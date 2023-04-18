from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError

from rooms import models as m
from rooms import serializers as s


class Rooms(APIView):
    def get(self, request):
        all_rooms = m.Room.objects.all()
        serializer = s.RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = s.RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                room = serializer.save(
                    founder=request.user  # 명시적으로 작성해줌 -> 여기서도 해줘야하는지 확인해보자
                )
                serializer = s.RoomDetailSerializer(room)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, id):
        try:
            return m.Room.objects.get(id=id)
        except m.Room.DoesNotExist:
            raise NotFound
    
    def get(self, request, id):
        room = self.get_object(id)
        serializer = s.RoomDetailSerializer(room)
        return Response(serializer.data)

    def put(self, request, id):
        room = self.get_object(id)
        serializer = s.RoomDetailSerializer(
            room,  # 기존에 있던 object
            data=request.data,  # 새롭게 받은 data
            partial=True,  # 부분적 업데이트
        )
        if serializer.is_valid():
            updated_room = serializer.save()
            return Response(
                s.RoomDetailSerializer(updated_room).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        room = self.get_object(id)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)