from django.urls import path
from API_TEST.views import UserCreateView
urlpatterns = [
    path("user/create", UserCreateView.as_view())
]