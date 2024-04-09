from django.urls import path
from .views import StudentCreateAPIView, ParentCreateAPIView, TeacherCreateAPIView, ParentListView , UserView

urlpatterns = [
    path('student/', StudentCreateAPIView.as_view(), name='student-create'),
    path('user/', UserView.as_view(), name='user-data'),
    path('parent/', ParentListView.as_view(), name='parent-list'),
    path('add-parent/', ParentCreateAPIView.as_view(), name='parent-create'),
    path('add-teacher/', TeacherCreateAPIView.as_view(), name='teacher-create'),
]