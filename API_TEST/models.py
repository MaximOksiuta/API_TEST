from django.db import models


# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=25)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=14, null=True)
    birthday = models.DateField(null=True)
    last_online = models.DateTimeField(null=False)


class Address(models.Model):
    address = models.CharField(max_length=255)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)


class DevelopStatus(models.Model):
    name = models.CharField(max_length=25)


class DeviceAccessStatus(models.Model):
    name = models.CharField(max_length=25)


class DeviceStatus(models.Model):
    name = models.CharField(max_length=25)


class DeviceTypes(models.Model):
    type_name = models.CharField(max_length=25)
    price = models.IntegerField()
    develop_status = models.ForeignKey('DevelopStatus', on_delete=models.CASCADE)
    device_access_status = models.ForeignKey('DeviceAccessStatus', on_delete=models.CASCADE)


class Firmwares(models.Model):
    name = models.CharField(max_length=25)
    version = models.CharField(max_length=10)
    device_type = models.ForeignKey('Device_types', on_delete=models.CASCADE)


class UserDevices(models.Model):
    device_name = models.CharField(max_length=30)
    device_type = models.ForeignKey('DeviceTypes', on_delete=models.CASCADE)
    status = models.ForeignKey('DeviceStatus', on_delete=models.CASCADE)
    firmware = models.ForeignKey('Firmwares', on_delete=models.CASCADE)
    owners = models.ManyToManyField('Users')
