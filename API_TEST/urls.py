from django.urls import path
from API_TEST.views import UserCreateView, GetUsersView

urlpatterns = [
    path("user/create", UserCreateView.as_view()),
    path("user/get_users", GetUsersView.as_view()),
    # path("user/<int:pk>", GetUserDetailsView())
]