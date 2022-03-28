from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from API_TEST.models import Users, Address, DevelopStatus, DeviceAccessStatus, DeviceStatus, DeviceTypes, Firmwares, \
    UserDevices
from API_TEST.serializers import UserSerializer, UserAuthSerializer, DevelopStatusSerializer, \
    DeviceAccessStatusSerializer, DeviceStatusSerializer, FirmwaresSerializer, \
    UserDeviceSerializer, AddressListSerializer, AddressPostSerializer, UserWithAddressesSerializer, \
    DeviceTypesPostSerializer, DeviceTypesListSerializer


class UsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class GetUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserAuthSerializer


class AddressListView(generics.ListAPIView):
    serializer_class = AddressListSerializer
    queryset = Address.objects.all()


class AddressCreateView(generics.CreateAPIView):
    serializer_class = AddressPostSerializer


class DevelopStatusView(generics.ListCreateAPIView):
    serializer_class = DevelopStatusSerializer
    queryset = DevelopStatus.objects.all()


class DeviceAccessStatusView(generics.ListCreateAPIView):
    serializer_class = DeviceAccessStatusSerializer
    queryset = DeviceAccessStatus.objects.all()


class DeviceStatusView(generics.ListCreateAPIView):
    serializer_class = DeviceStatusSerializer
    queryset = DeviceStatus.objects.all()


# class DeviceTypesView(generics.ListCreateAPIView):
#     serializer_class = DeviceTypesSerializer
#     queryset = DeviceTypes.objects.all()
class DeviceTypesCreateView(generics.CreateAPIView):
    serializer_class = DeviceTypesPostSerializer


class DeviceTypesListView(generics.ListAPIView):
    serializer_class = DeviceTypesListSerializer
    queryset = DeviceTypes.objects.all()

class FirmwaresView(generics.ListCreateAPIView):
    serializer_class = FirmwaresSerializer
    queryset = Firmwares.objects.all()


class UserDevicesView(generics.ListCreateAPIView):
    serializer_class = UserDeviceSerializer
    queryset = UserDevices.objects.all()


class UserWithAddressesView(generics.RetrieveAPIView):
    serializer_class = UserWithAddressesSerializer
    queryset = Users.objects.all()
