from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedRelatedField, 
    StringRelatedField
)
from users import models as m

# ref. https://www.django-rest-framework.org/api-guide/relations

class PublicUserSerializer(ModelSerializer):
    # position = StringRelatedField(many=True)
    # portfolio = HyperlinkedRelatedField(read_only=True)

    class Meta:
        model = m.User
        fields = (
            "name",
            "nickname",
            "introduce",
            "region",
            "available_schedule",
            "career",
            "profile_file_key",
            "plant_stage",
            "is_host",
            "position",  # foreign key
            "portfolio",  # in Portfolio
        )

class PrivateUserSerializer(ModelSerializer):
    # portfolio = HyperlinkedRelatedField(read_only=True)

    class Meta:
        model = m.User
        fields = (
            "name",
            "email",
            "password",
            "nickname",
            "introduce",
            "region",
            "available_schedule",
            "career",
            "profile_file_key",
            "role",
            "plant_stage",
            "is_host",
            "position",  # foreign key
            "portfolio",  # in Portfolio
            "room_founder",  # in Room
        )