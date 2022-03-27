from django.urls import path
from API_TEST.views import GetUsersView, GetUserDetailsView

urlpatterns = [
    # path("user", UserCreateView.as_view()),
    path("user/", GetUsersView.as_view()),
    path("user/<int:pk>", GetUserDetailsView.as_view())
]