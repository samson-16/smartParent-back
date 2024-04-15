from django.shortcuts import render
from .models import User, Student , Parent, Teacher
from rest_framework import generics, serializers
from .serializers import UserSerializer , StudentSerializer, ParentSerializer, TeacherSerializer, ParentListSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password , check_password
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model , authenticate
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('id')
        if user_id:
            queryset = queryset.filter(id=user_id)
        return queryset
class UserEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class StudentCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        grade = self.request.query_params.get('grade')
        section = self.request.query_params.get('section')

        if grade and section:
            queryset = queryset.filter(grade=grade, section=section)
        elif grade:
            queryset = queryset.filter(grade=grade)
        elif section:
            queryset = queryset.filter(section=section)

        return queryset

class ParentCreateAPIView(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated] 

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
                'password': password,
            }
            print(password) 
            user_serializer = UserSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.save()
            serializer.save(user=user)

            parent = f"{user.first_name} {user.last_name}"
            username  = user.email
            parent_password = password 
            link = "http://localhost:5173/"
            context = {
                "parent": parent, 
                "username": username, 
                "password": parent_password,
                "link" : link
            }
            emailsubject = 'Your Account Details'
            html_msg =  render_to_string("email.html", context=context)
            plain_msg = strip_tags (html_msg)
            message = EmailMultiAlternatives(
                subject=emailsubject, 
                body= plain_msg,
                from_email = settings.DEFAULT_FROM_EMAIL , 
                to= [user.email]
                )
            message.attach_alternative(html_msg , "text/html")
            message.send()

            """ from_email = 
            to_email = user.email
            send_mail(subject, message, from_email, [to_email]) """
        else:
            raise serializers.ValidationError("Missing required fields")
        
class ParentListView(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('id')
        grade = self.request.query_params.get('grade')
        section = self.request.query_params.get('section')

        if user_id:
            queryset = queryset.filter(user__id=user_id)
        if grade:
            queryset = queryset.filter(children__grade=grade)
        if section:
            queryset = queryset.filter(children__section=section)

        return queryset.distinct()

class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated] 

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


class TeacherListAPIView(generics.ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        queryset = Teacher.objects.all()
        user_id = self.request.query_params.get('id')
        if user_id:
            queryset = queryset.filter(user__id=user_id)
        return queryset


class TokenObtainPairView(APIView):
    permission_classes = [IsAuthenticated] 
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
