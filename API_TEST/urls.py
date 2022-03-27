from django.urls import path
from API_TEST.views import UsersView, GetUserDetailsView, DevelopStatusView, DeviceAccessStatusView, \
    DeviceStatusView, FirmwaresView, UserDevicesView, AddressListView, AddressCreateView

urlpatterns = [
    # path("user", UserCreateView.as_view()),
    path("user/", UsersView.as_view()),
    path("user/<int:pk>", GetUserDetailsView.as_view()),
    path("address/list", AddressListView.as_view()),
    path("address/create", AddressCreateView.as_view())
    # path("develop_status/", DevelopStatusView.as_view()),
    # path("device_access_status/", DeviceAccessStatusView.as_view()),
    # path("device_status/", DeviceStatusView.as_view()),
    # path("device_types/", DeviceTypesView.as_view()),
    # path("firmware/", FirmwaresView.as_view()),
    # path("devices/", UserDevicesView.as_view())

]