from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """Project_Room Model Definition"""

    class ActiveTimeChoices(models.IntegerChoices):
        MORNING = 9
        AFTERNOON = 12
        EVENING = 18
        ALL_TIME  = 24

    name = models.CharField(
        max_length=256,
    )
    introduce = models.TextField()
    recruitment_period = models.DateTimeField()
    active_time = models.PositiveIntegerField(
        default=0,
        choices=ActiveTimeChoices.choices,
    )
    main_file_key = models.URLField(blank=True)  # For project_main_img URL
    founder = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="room_founder",
    )
    # 모집 여부 : router에서 직접 구현해서 반환하기
    # count : router에서 직접 구현해서 반환


# Connection table
class RoomPosition(models.Model):
    """Connection Project_Room and Position Model Definition"""
    max_applicant = models.IntegerField()
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="roomposition",
    )
    position = models.ForeignKey(
        "users.Position",
        on_delete=models.CASCADE,
        related_name="roomposition",
    )


# Connection table
class Mark(models.Model):
    """Connection User and Project_Room Model Definition"""
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="mark",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="mark",
    )


class Hashtag(CommonModel):
    """Hashtag (about project) Model Definition"""
    name = models.CharField(
        max_length=256,
        primary_key=True,
    )
    room = models.ManyToManyField(
        "rooms.Room",
        related_name="hashtags",
    )
    user = models.ManyToManyField(
        "users.User",
        related_name="hashtags",
    )

# DONE: hashtag와 room에 대해서 manytomany 필드를 사용해야함, 그래야 serializer에서 불러올 수 있다.