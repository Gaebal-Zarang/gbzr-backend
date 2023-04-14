from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel


"""
[User에서 기본적으로 제공하는 필드]
* id (pk, not null, int)
* username (not null, char)
* email (char-emailField)
* password (not null)
* last_login (not null, dateTime)
* date_joined (not null, dateTime)
"""

class User(AbstractUser):
    """User model Definition"""
    #ref. https://velog.io/@minhyuk_ko/TIL-Enum-class-IntegerChoices
    class RoleChoices(models.IntegerChoices):
        Owner = 50
        Admin = 25
        User = 0
    
    class RegionChoices(models.IntegerChoices):
        Seoul = 10
        Incheon = 20
        Daejeon = 30
        Daegu = 40
        Gwangju = 50
        Jejudo = 60
        Ulsan = 70
        Busan = 80
    
    class PlantStagesChoices(models.IntegerChoices):
        Sprout = 0  # 새싹
        Peak = 10  # 봉우리
        Flower = 20  # 꽃


    name = models.CharField(
        max_length=128,
    )
    email = models.EmailField(
        verbose_name="email",
        max_length=256,
        unique=True,
    )
    nickname = models.CharField(
        max_length=128,
        default="",
    )
    introduce = models.TextField()
    region = models.IntegerField(
        choices=RegionChoices.choices,
        default=False,
    )
    available_schedule = models.BooleanField(
        default=False,
    )
    career = models.PositiveIntegerField(
        default=0,
    )  # It allows zero.
    profile_file_key = models.URLField(blank=True)  # For profile_img URL
    role = models.IntegerField(
        default=0,
        choices=RoleChoices.choices,
    )
    plant_stage = models.PositiveIntegerField(
        default=0,
        choices=PlantStagesChoices.choices,
    )
    is_host = models.IntegerField(
        default=0,
    )  # 방장 (room number가 입력되면 방장임)
    position = models.ForeignKey(
        "users.Position",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_position",
    )


class Position(models.Model):
    """Position Model Definition"""
    class PositionChoices(models.TextChoices):
        MANAGER = ("manager", "Manager")
        DESIGNER = ("designer", "Designer")
        FRONTEND = ("frontend", "Frontend")
        BACKEND = ("backend", "Backend")
    
    position = models.CharField(
        max_length=32,
        choices=PositionChoices.choices,
        default=False,
    )
    count = models.IntegerField()


class Portfolio(CommonModel):
    """Portfolio Model Definition"""
    link = models.URLField(
        primary_key=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="portfolio",
    )


class UserLoginLog(models.Model):
    """User_Login_Log Model Definition"""
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="userloginlog",
    )
    ip = models.CharField(
        max_length=256,
    )



