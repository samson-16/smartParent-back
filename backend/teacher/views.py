from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import ExamResult,Assignment
from .serializer import ExamResultSerializer,AssignmentSerializer

class ExamResultListCreate(generics.ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class ExamResultRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class AssignmentListCreate(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
