from rest_framework import serializers
from API_TEST.models import Users, Address, DevelopStatus, DeviceAccessStatus, DeviceStatus, DeviceTypes, Firmwares, \
    UserDevices


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = 'user_name'


class AddressSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(many=False)

    class Meta:
        model = Address
        fields = ('address', 'user')


class DevelopStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopStatus
        fields = '__all__'


class DevelopStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopStatus
        fields = 'name'


class DeviceAccessStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAccessStatus
        fields = '__all__'


class DeviceAccessStatusnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAccessStatus
        fields = 'name'


class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = '__all__'


class DeviceStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = 'name'


class DeviceTypesSerializer(serializers.ModelSerializer):
    develop_status = DevelopStatusNameSerializer(many=False)
    device_access_status = DeviceAccessStatusnameSerializer(many=False)

    class Meta:
        model = DeviceTypes
        fields = ('id', 'type_name', 'price', 'develop_status', 'device_access_status')


class DeviceTypesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTypes
        fields = 'type_name'


class FirmwaresSerializer(serializers.ModelSerializer):
    device_type = DeviceTypesNameSerializer(many=False)

    class Meta:
        model = Firmwares
        fields = ('id', 'name', 'version', 'device_type')


class FirmwaresNameSerializer(serializers.ModelSerializer):
    device_type = DeviceTypesNameSerializer(many=False)

    class Meta:
        model = Firmwares
        fields = ('id', 'name', 'version', 'device_type')


class UserDeviceSerializer(serializers.ModelSerializer):
    device_type = DeviceTypesNameSerializer(many=False)
    status = DeviceStatusNameSerializer(many=False)
    firmware = FirmwaresNameSerializer(many=False)

    class Meta:
        model = UserDevices
        fields = ('id', 'device_name', 'device_type', 'status', 'firmware')
