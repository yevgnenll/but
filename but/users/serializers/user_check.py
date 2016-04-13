from rest_framework import serializers

from django.conf import settings


class UserCheckModelSerialize(serializers.ModelSerializer):

    class Meta:

        model = settings.AUTH_USER_MODEL
