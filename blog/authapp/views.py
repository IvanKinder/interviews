from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from authapp.forms import UserLoginForm, UserRegisterForm


@csrf_exempt
def login(request):
    """Представление для входа в блог"""
    login_form = UserLoginForm(data=request.POST)
    next_url = request.GET.get('next', '')
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('mainapp:home'))
    content = {'login_form': login_form, 'next': next_url}
    return render(request, 'authapp/login.html', content)


def logout(request):
    """Loguot"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:home'))


def register(request):
    """Регистрация на сайте"""
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)
