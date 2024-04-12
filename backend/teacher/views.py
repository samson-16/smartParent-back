from rest_framework import generics , viewsets
from .models import Task, Exam, ExamResult, Resource
from .serializers import TaskSerializer, ExamSerializer, ExamResultSerializer, ResourceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.http import HttpResponse, FileResponse,Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404

class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Task.objects.all()
        section = self.request.query_params.get('section')

        if section:
            queryset = queryset.filter(details__section=section)

        return queryset

class ExamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [AllowAny]

class ExamResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    permission_classes = [AllowAny]

class ResourceCreateAPIView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [AllowAny]

def download_resource(request, resource_id):
    uploaded_file = Resource.objects.get(pk=resource_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response