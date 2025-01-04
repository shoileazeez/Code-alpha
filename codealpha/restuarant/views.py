from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
# Create your views here.


class RegistrationView(APIView):
    permission_classes= [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "registation was successful please check your email for otp",
                "user": user.id
            }, status= status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )