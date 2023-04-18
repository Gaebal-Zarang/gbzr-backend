from rest_framework.serializers import ModelSerializer
from rooms import models as m
from users.serializers import TinyUserSerializer


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = m.Room
        fields = (
            "name",
            "hashtags",
            "recruitment_period",
        )



class RoomDetailSerializer(ModelSerializer):
    # [custom serializer]
    founder = TinyUserSerializer(read_only=True)
    # amenities = AmenitySerializer(
    #     read_only=True,
    #     many=True  # many=True: array인 경우 사용
    # )
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = m.Room
        fields = "__all__"