from django.db import models
from django.contrib.auth.models import AbstractUser

# TODO: user table
class User(AbstractUser):
    """
    [User에서 기본적으로 제공하는 필드]
    * id (pk, not null, int)
    * username (not null, char)
    * email (char-emailField)
    * password (not null)
    * last_login (not null, dateTime)
    * date_joined (not null, dateTime)
    """
    class LoginChoices(models.TextChoices):
        EMAIL = ("email", "Email")
        KAKAO = ("kakao", "Kakao")
        NAVER = ("naver", "Naver")
        APPLE = ("apple", "Apple")


    #ref. https://velog.io/@minhyuk_ko/TIL-Enum-class-IntegerChoices
    class RoleChoices(models.IntegerChoices):
        Owner = 50
        Admin = 25
        User = 0

    # user_id = models.AutoField(
    #     primary_key=True,
    #     unique=True,
    # )  # id는 자동생성 필드

    # nickname = models.CharField(
    #     max_length=15,
    # )  # 별명
    # self_introduce = models.TextField()  # 자기소개
    # region = models.CharField(
    #     max_length=15,
    # )  # 지역
    # position = models.CharField(
    #     max_length=17,
    #     choices=POSITION_CHOICES,
    # )  # 프로젝트 포지션
    # expect_to_join = models.BooleanField(
    #     default=False,
    # )  # 현재 참여 가능 여부 (기본값: 현재 참여 불가능)
    # career = models.IntegerField(
    #     default=0,
    # )  # 경력(연차)
    # is_host = models.BooleanField(
    #     default=False,
    # )  # 방장 (기본값: 일반유저)
    # login_method = models.CharField(
    #     max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    # )  # 로그인 방법(플랫폼)

    class Meta:
        db_table = 'user'


# DONE: position table
class Position(models.Model):
    """Position Model Definition"""
    class PositionChoices(models.TextChoices):
        MANAGER = ("manager", "Manager")
        DESIGNER = ("designer", "Designer")
        BACKEND_ENGINEER = ("backend_engineer", "Backend_Engineer")
        FRONTEND_ENGINEER = ("frontend_engineer", "Frontend_Engineer")
        # ENGINEER = (
        #     BACKEND = (
        #         "backend_engineer", "Backend_Engineer"
        #     ),
        #     FRONTEND = (
        #         "frontend_engineer", "Frontend_Engineer"
        #     )
        # )
    
    position = models.CharField(
        max_length=18,
        choices=PositionChoices.choices,
    )
    count = models.IntegerField(
        null=True, blank=True,
    )

# TODO: user_login_log table



# TODO: portfolio table