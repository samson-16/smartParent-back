from rest_framework import generics
from .models import Task, Exam, ExamResult
from .serializers import TaskSerializer, ExamSerializer, ExamResultSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class ExamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [AllowAny]

class ExamResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    permission_classes = [AllowAny]
