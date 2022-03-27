from rest_framework import serializers
from API_TEST.models import Users


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
