from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated

from auths import serializers as s
from auths import models as m


class Signup(APIView):
    def post(self, request):
        name = request.data.get("name")
        email = request.data.get("email")
        raw_password = request.data.get("password")

        if not email or not raw_password:
            raise ParseError
        
        serializer = s.SignupUserSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(raw_password)  # hashed pw
            user.save()
            serializer = s.SignupUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            raise ParseError
        
        # validation: email이 맞지 않은 경우, 접근 권한 여부 확인 후 에러발생
        user = authenticate(
            request,
            email=email,
            password=password,
        )
        if user:
            login(request, user)
            return Response(
                # QUESTION: access token이 반환되어야하는거 아닌가?
                {"success": "Welcome!"},
                status=status.HTTP_200_OK,
            )
        else:
            # QUESTION: Response로 보내면 status_code가 200인가?
            return Response(
                {"error": "wrong password"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"success": "bye!"}, 
            status=status.HTTP_200_OK,
        )