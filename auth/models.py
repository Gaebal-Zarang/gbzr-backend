from django.db import models
import uuid


class Oauth(models.Model):

    """OAuth2 Model Definition"""
    # ref. About Composite Primary Keys, PostgreSQL and Django
    #   - https://www.crunchydata.com/blog/composite-primary-keys-postgresql-and-django
    #   - https://everyevery-blog.tumblr.com/post/29123180487/django-orm%EC%97%90%EC%84%9C-composite-primary-key-%EC%82%AC%EC%9A%A9

    # [question] uuidfield
    uid = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=False,
        max_length=128,
    )
    provider_type = models.CharField(
        primary_key=True,
        unique=False,
        max_length=128,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="oauth",
    )
    # ref. About related_name: https://velog.io/@brighten_the_way/Django%EC%99%80-Reverse-relations%EA%B3%BC-Relatedname


    # 로그인 방법(플랫폼)
    # class LoginChoices(models.TextChoices):
    #     EMAIL = ("email", "Email")
    #     KAKAO = ("kakao", "Kakao")
    #     NAVER = ("naver", "Naver")
    #     APPLE = ("apple", "Apple")

    # login_method = models.CharField(
    #     max_length=64, 
    #     choices=LoginChoices.choices, 
    #     default="email"
    # )  
