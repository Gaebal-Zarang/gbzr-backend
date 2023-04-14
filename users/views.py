from django.shortcuts import render
import jwt
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated

from users import models as m
from users import serializers as s


class Users(APIView):
    permission_classes = [IsAuthenticated]  # owner권한

    def get(self, request):
        '''모든 유저의 정보 조회 (권장하지않음)'''
        pass


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = s.PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = s.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = s.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request):
        # 자기 자신 탈퇴하기
        user = request.user
        # user에 대한 검증, serializer 이용해서
        serializer = s.PrivateUserSerializer(user)
        if serializer.is_valid():
            user.delete()
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class SelectUserID(APIView):
    # 다른 회원 탈퇴시키기
    permission_classes = [IsAuthenticated]  # owner권한

    def delete(self, request, id):
        select_user = self.get_object(id)
        select_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SelectUserName(APIView):
    def get(self, request, name):
        try:
            user = m.User.objects.get(name=name)
        except m.User.DoesNotExist:
            raise NotFound
        serializer = s.PublicUserSerializer(user)
        return Response(serializer.data)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError
        
        if user.check_password(old_password):  # validate hashed pw
            user.set_password(new_password)  # hashed new_pw
            user.save()  # saving user object to db
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError


class ChangeUserRole(APIView):
    # permission_classes = [IsAuthenticated]  # 관리자급
    def put(self, request, id):
        pass
    pass