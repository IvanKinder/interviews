from django.forms import ModelForm

from authapp.models import ReferalUser


class ReferalUserLoginForm(ModelForm):
    class Meta:
        model = ReferalUser
        fields = ('phone_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
