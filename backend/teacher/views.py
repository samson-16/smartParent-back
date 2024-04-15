from rest_framework import generics , viewsets
from .models import Task, Exam, ExamResult, Resource
from .serializers import TaskSerializer, ExamSerializer, ExamResultSerializer, ResourceSerializer, TaskListSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.http import HttpResponse


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()
        section = self.request.query_params.get('section')
        teacher = self.request.query_params.get('teacher')

        if section:
            queryset = queryset.filter(details__section=section)
        if teacher:
            queryset = queryset.filter(details__teacher=teacher)
        return queryset

class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class ExamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

class ExamResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated]
class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class ResourceCreateAPIView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAuthenticated]
def download_resource(request, resource_id):
    uploaded_file = Resource.objects.get(pk=resource_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response