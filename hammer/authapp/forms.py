from django.forms import ModelForm
from django import forms

from authapp.models import ReferalUser


class ReferalUserLoginForm(ModelForm):
    """ форма для входа по номеру телефона """

    class Meta:
        model = ReferalUser
        fields = ('phone_number',)


class ReferalUserCodeForm(forms.Form):
    """ форма для введения кода """

    code = forms.CharField(max_length=4, label='Код')


class InputCodeForm(ModelForm):
    """ форма для ввода инвайт кода """

    class Meta:
        model = ReferalUser
        fields = ('invite_code',)
