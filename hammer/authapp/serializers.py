from rest_framework import serializers

from authapp.models import ReferalUser


class ReferalUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для юзеров """

    class Meta:
        model = ReferalUser
        fields = '__all__'
