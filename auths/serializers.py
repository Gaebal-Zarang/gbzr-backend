from rest_framework.serializers import ModelSerializer
from users import models as m


class SignupUserSerializer(ModelSerializer):
    class Meta:
        model = m.User
        exclude = (
            "id",
            "password",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
            "username",
            "nickname",
            "introduce",
            "username",
        )  # 사용하지 않을 fields

        # fields = (
        #     "name",
        #     "email",
        #     "password",
        # )

        # fields = "__all__"