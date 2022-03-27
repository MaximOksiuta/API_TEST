from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from API_TEST.models import Users
from API_TEST.serializers import UserCreateSerializer, UserListSerializer, UserAuthSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class GetUsersView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = Users


class GetUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserAuthSerializer
