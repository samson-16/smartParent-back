from django.shortcuts import render
from .models import User, Student , Parent, Teacher
from rest_framework import generics
from .serializers import UserSerializer , StudentSerializer, ParentSerializer, TeacherSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth.hashers import make_password

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

class ParentCreateAPIView(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        parent_first_name = self.request.data['first_name']
        child_id = self.request.data['children'][0]
        password = f"{parent_first_name}{child_id}"
        user_data = {
            'username': self.request.data['email'],
            'first_name': self.request.data['first_name'],
            'last_name': self.request.data['last_name'],
            'email': self.request.data['email'],
            'phone_number': self.request.data['phone_number'],
            'role': 'parent',
            'password': make_password(password),
        }
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        serializer.save(user=user)

class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        teacher_first_name = self.request.data['first_name']
        teacher_phone =  self.request.data['phone_number'],
        password = f"{teacher_first_name}{teacher_phone}"
        user_data = {
            'username': self.request.data['email'],
            'first_name': self.request.data['first_name'],
            'last_name': self.request.data['last_name'],
            'email': self.request.data['email'],
            'phone_number': self.request.data['phone_number'],
            'role': 'teacher',
            'password': make_password(password),
        }
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        serializer.save(user=user)