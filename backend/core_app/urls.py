from django.urls import path
from .views import StudentCreateAPIView, ParentCreateAPIView, TeacherCreateAPIView, ParentListView , UserView , TeacherListAPIView,UserEditView

urlpatterns = [
    path('student/', StudentCreateAPIView.as_view(), name='student-create'),
    path('user/', UserView.as_view(), name='user-data'),
    path('user/<int:pk>/', UserEditView.as_view(), name='user-edit'),
    path('parent/', ParentListView.as_view(), name='parent-list'),
    path('add-parent/', ParentCreateAPIView.as_view(), name='parent-create'),
    path('add-teacher/', TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('teachers/', TeacherListAPIView.as_view(), name='teacheers-list'),
]