from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/auth/", include("auths.urls")),
    path("v1/users/", include("users.urls")),
]