import random
import string
import time

from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView

from authapp.forms import ReferalUserLoginForm, ReferalUserCodeForm, InputCodeForm
from authapp.models import ReferalUser
from authapp.serializers import ReferalUserSerializer, AuthTokenSerializer


TMP_CODE = []


def generate_alphanum_random_string(length):
    """ генератор случайной строки с проверкой на уникальность """

    users = ReferalUser.objects.all()
    codes = set()
    for user in users:
        codes.add(user.code)
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    if rand_string not in codes:
        return rand_string
    return generate_alphanum_random_string(length)


def login(request):
    """ представление для входа """

    code_form = ReferalUserCodeForm(data=request.POST)
    login_form = ReferalUserLoginForm(data=request.POST)
    if request.method == 'POST':
        phones = []
        for user in ReferalUser.objects.all():
            phones.append(user.phone_number)
        phone_number = int(request.POST.get('phone_number'))
        if phone_number not in phones:
            users_count = len(ReferalUser.objects.all())
            user = ReferalUser.objects.create_user(username=f'user{users_count + 1}', phone_number=phone_number,
                                                   code=generate_alphanum_random_string(6))
        else:
            user = ReferalUser.objects.get(phone_number=phone_number)
        if user and user.is_active:
            auth.login(request, user)

        TMP_CODE.append(generate_alphanum_random_string(4))
        content = {'tmp_code': TMP_CODE[0], 'code_form': code_form}
        time.sleep(3)
        return render(request, 'authapp/code.html', content)
    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)


@user_passes_test(lambda u: u.is_authenticated)
def tmp_code(request):
    """ представление для подтверждения кода """

    code_form = ReferalUserCodeForm(data=request.POST)
    if request.method == 'POST':
        tmp_code = request.POST.get('code')
        if len(TMP_CODE) > 0 and tmp_code == TMP_CODE[0]:
            content = {'data': True}
            TMP_CODE.pop(0)
        else:
            content = {'data': False}
        return render(request, 'authapp/success.html', content)
    content = {'code_form': code_form}
    return render(request, 'authapp/code.html', content)


@user_passes_test(lambda u: u.is_authenticated)
def user(request):
    """ Представление профиля пользователя """

    invite_code_form = InputCodeForm(data=request.POST)
    user = ReferalUser.objects.get(username=request.user)
    codes = []
    message = 0
    invited_users = []
    for u in ReferalUser.objects.all():
        codes.append(u.code)
        if u.invite_code == user.code:
            invited_users.append(u.phone_number)
    content = {'form': invite_code_form, 'user': request.user, 'invite_code': user.invite_code, 'message': message,
               'invited_users': invited_users}
    if request.method == 'POST':
        if request.POST.get('invite_code') in codes:
            user.invite_code = request.POST.get('invite_code')
            user.save()
            message = 1
        else:
            message = 2
        content = {'form': invite_code_form, 'user': user, 'message': message}
    return render(request, 'authapp/user.html', content)


class ReferalUserAPIView(ModelViewSet):
    """ api view для юзера """

    queryset = ReferalUser.objects.all()
    serializer_class = ReferalUserSerializer

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @classmethod
    def get_extra_actions(cls):
        return []


class MyAuthToken(APIView):
    """ Переопределение api view для токена """

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="phone_number",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="phone_number",
                        description="Valid phone_number for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


obtain_auth_token = MyAuthToken.as_view()
