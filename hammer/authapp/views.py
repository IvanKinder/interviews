import random
import string

from django.contrib import auth
from django.shortcuts import render

from authapp.forms import ReferalUserLoginForm
from authapp.models import ReferalUser


CODES = set()


def generate_alphanum_random_string(length):
    """ генератор случайной строки с проверкой на уникальность """

    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    if rand_string not in CODES:
        CODES.add(rand_string)
        return rand_string
    return generate_alphanum_random_string(length)




def login(request):
    login_form = ReferalUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        phone_number = request.POST.get('phone_number')
        users_count = len(ReferalUser.objects.all())
        user = ReferalUser.objects.create_user(username=f'user{users_count + 1}', phone_number=phone_number)
        print(user)
        if user and user.is_active:
            auth.login(request, user)
    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)
