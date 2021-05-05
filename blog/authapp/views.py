from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView, UpdateView

from authapp.forms import UserRegisterForm, UserLoginForm, UserEditForm


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            print('успешно')
            print(user)
        else:
            print('ошибка')
        return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = UserRegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def login(request):
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
            return HttpResponseRedirect(reverse('authapp:update_user', args=[request.user.pk]))
    content = {'login_form': login_form, 'next': next_url}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


class UserUpdateView(UpdateView):
    model = User
    template_name = 'authapp/user_page.html'
    form_class = UserEditForm

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @method_decorator(user_passes_test(lambda u: u.is_authenticated))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
