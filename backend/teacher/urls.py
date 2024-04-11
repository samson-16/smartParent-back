from django.urls import path
from .views import TaskListCreateAPIView, ExamListCreateAPIView, ExamResultListCreateAPIView , ResourceCreateAPIView, download_resource

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('exams/', ExamListCreateAPIView.as_view(), name='exam-list-create'),
    path('exam-results/', ExamResultListCreateAPIView.as_view(), name='exam-result-list-create'),
    path('resource/', ResourceCreateAPIView.as_view(), name='resource'),
    path('resource/<int:resource_id>/download/', download_resource, name='download_resource'),
]

