from django.urls import path
from API_TEST.views import UserCreateView, GetUsersView, GetUserDetailsView

urlpatterns = [
    path("user", UserCreateView.as_view()),
    path("users/get_all", GetUsersView.as_view()),
    path("user/<int:pk>", GetUserDetailsView.as_view())
]