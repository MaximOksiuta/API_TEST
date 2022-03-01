from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from API_TEST.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
