from django.urls import path
from rooms import views

app_name = "rooms"

urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:id>", views.RoomDetail.as_view()),
]