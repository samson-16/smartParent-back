from django.shortcuts import render
from .models import User, Student , Parent, Teacher
from rest_framework import generics, serializers
from .serializers import UserSerializer , StudentSerializer, ParentSerializer, TeacherSerializer, ParentListSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth.hashers import make_password , check_password
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model , authenticate

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('id')
        if user_id:
            queryset = queryset.filter(id=user_id)
        return queryset

class StudentCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

class ParentCreateAPIView(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        parent_first_name = self.request.data.get('first_name')
        children = self.request.data.get('children')
        if parent_first_name and children:
            password = parent_first_name + str(children[0])
            user_data = {
                'username': self.request.data.get('email'),
                'first_name': parent_first_name,
                'last_name': self.request.data.get('last_name'),
                'email': self.request.data.get('email'),
                'phone_number': self.request.data.get('phone_number'),
                'role': 'parent',
                'password': make_password(password),
            }
            print(password)
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            serializer.save(user=user)
        else:
            raise serializers.ValidationError("Missing required fields")
        
class ParentListView(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('id')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset

class TeacherCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        teacher_first_name = self.request.data.get('first_name')
        teacher_phone =  self.request.data.get('phone_number')
        if teacher_first_name and teacher_phone:
            password = teacher_first_name + str(teacher_phone)
            print(password)
            user_data = {
                'username': self.request.data.get('email'),
                'first_name': teacher_first_name,
                'last_name': self.request.data.get('last_name'),
                'email': self.request.data.get('email'),
                'phone_number': teacher_phone,
                'role': 'teacher',
                'password': password,
            }
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            serializer.save(user=user)
        else:
            raise serializers.ValidationError("Missing required fields")

class TokenObtainPairView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })
