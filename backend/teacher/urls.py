from django.urls import path
from .views import ( ExamListCreateAPIView, 
                    ExamResultListCreateAPIView, ExamDetailView, 
                    TaskDetailView, ExamResultDetailView,ResourceCreateAPIView,download_resource , TaskCreateAPIView, TaskListAPIView)

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('add-task/', TaskCreateAPIView.as_view(), name='add-task'),
    path('exams/', ExamListCreateAPIView.as_view(), name='exam-list-create'),
    path('exam-results/', ExamResultListCreateAPIView.as_view(), name='exam-result-list-create'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('exam-results/<int:pk>/', ExamResultDetailView.as_view(), name='exam-result-detail'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('resource/', ResourceCreateAPIView.as_view(), name='resource'),
    path('resource/<int:resource_id>/download/', download_resource, name='download_resource'),
]
