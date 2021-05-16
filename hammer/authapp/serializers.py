import random
import string

from django.contrib import auth
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

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


class ReferalUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для юзеров """

    class Meta:
        model = ReferalUser
        fields = '__all__'


class AuthTokenSerializer(serializers.Serializer):
    """ Переопределение сериализатора для токена """

    phone_number = serializers.IntegerField(
        label=_("Phone_number"),
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        """ Переопределение валидации для токена """

        phone_number = attrs.get('phone_number')
        if phone_number:
            try:
                user = ReferalUser.objects.get(phone_number=phone_number)
            except Exception:
                users_count = len(ReferalUser.objects.all())
                user = ReferalUser.objects.create_user(username=f'user{users_count + 1}', phone_number=phone_number,
                                                       code=generate_alphanum_random_string(6))
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
