import random
import string

from django.contrib import auth
from django.shortcuts import render

from authapp.forms import ReferalUserLoginForm
from authapp.models import ReferalUser


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

    login_form = ReferalUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        phone_number = request.POST.get('phone_number')
        users_count = len(ReferalUser.objects.all())
        user = ReferalUser.objects.create_user(username=f'user{users_count + 1}', phone_number=phone_number,
                                               code=generate_alphanum_random_string(6))
        if user and user.is_active:
            auth.login(request, user)
    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def tmp_code(request):
    """ представление для подтверждения кода """

    # code_form = ReferalUserCodeForm(data=request.POST)
    # print(request.__dict__)
    if request.method == 'POST':
        tmp_code = request.POST.__dict__
        print(tmp_code)
        # phone_number = request.POST.get('phone_number')
        # phones = set()
        # users = ReferalUser.objects.all()
        # for user in users:
        #     phones.add(user.phone_number)
        # user = ReferalUser.objects.create_user(username=f'user{users_count + 1}', phone_number=phone_number,
        #                                        code=generate_alphanum_random_string(6))
        # if user and user.is_active:
        #     auth.login(request, user)
    # content = {'code_form': code_form}
    return render(request, 'authapp/code.html')
