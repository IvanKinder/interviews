from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from authapp.models import ReferalUser


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
            user = ReferalUser.objects.get(phone_number=phone_number)
            print(user)
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
