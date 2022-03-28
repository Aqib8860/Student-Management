from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import generics
from .serializers import *
from .permissions import *
from .models import User
import jwt, datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


# Login View For Access Token
class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = CustomTokenObtainPairSerializer


# User Registration for all teacher and student only. Admin is superuser
class RegisterView(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message':"Register Success",
            'data': serializer.data,
        }
        return response


# Add Student View
class AddStudentView(APIView):

    permission_classes = (IsAuthenticated, IsTeacher) # Creating Custom permission classes for Teacher & Admin

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message':"Register Success",
            'data': serializer.data,
        }
        return response


# View STudent List with permission of Teacher & Admin Only
class StudentListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated, IsTeacher, IsAdmin) # Creating Custom permission classes in permission.py file for Teacher & Admin

    def get(self, request):
        queryset = self.queryset.filter(is_student=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# List All Students and Teacher by Admin
class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer
    permission_classes = (IsAuthenticated, IsAdmin)
    http_method_names = ['get', 'head', 'options']
