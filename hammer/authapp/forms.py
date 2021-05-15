from django.forms import ModelForm, Form

from authapp.models import ReferalUser


class ReferalUserLoginForm(ModelForm):
    """ форма для входа по номеру телефона """

    class Meta:
        model = ReferalUser
        fields = ('phone_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class ReferalUserCodeForm(Form):
#     """ форма для введения кода """
#
#     class Meta:
#         fields = ('tmp_code',)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
