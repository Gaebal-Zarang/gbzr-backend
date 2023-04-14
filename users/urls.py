from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "users"

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("<int:id>", views.SelectUserID.as_view()),
    path("@<str:name>", views.SelectUserName.as_view()),  # '/me' 또한 조건을 만족하기 때문에, 순서 중요!
    path("change-password", views.ChangePassword.as_view()),
    path("<int:id>/role", views.ChangeUserRole.as_view()),
]