from django.urls import path
from .views import StudentCreateAPIView, ParentCreateAPIView, TeacherCreateAPIView

urlpatterns = [
    path('student/', StudentCreateAPIView.as_view(), name='student-create'),
    path('parent/', ParentCreateAPIView.as_view(), name='parent-create'),
    path('teacher/', TeacherCreateAPIView.as_view(), name='teacher-create'),
]