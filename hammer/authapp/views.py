import random
import string
import time

from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ReferalUserLoginForm, ReferalUserCodeForm, InputCodeForm
from authapp.models import ReferalUser


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
    if request.method == 'POST':
        codes = []
        for user in ReferalUser.objects.all():
            codes.append(user.code)
        user = ReferalUser.objects.get(username=request.user)
        if request.POST.get('invite_code') in codes:
            user.invite_code = request.POST.get('invite_code')
            user.save()
            content = {'user': user, 'invite_code': user.invite_code}
            return render(request, 'authapp/user.html', content)
    content = {'form': invite_code_form, 'user': request.user, 'invite_code': request.user.invite_code}
    return render(request, 'authapp/user.html', content)
