from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.GradeListCreateAPIView.as_view(), name='grade-list'),
    path('grades/<int:pk>/', views.GradeRetrieveUpdateDestroyAPIView.as_view(), name='grade-detail'),
    path('sections/', views.SectionListCreateAPIView.as_view(), name='section-list'),
    path('sections/<int:pk>/', views.SectionRetrieveUpdateDestroyAPIView.as_view(), name='section-detail'),
    path('subjects/', views.SubjectListCreateAPIView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name='subject-detail'),
    path('class-subjects/', views.ClassSubjectListAPIView.as_view(), name='class-subject-list'),
    path('add-class-subjects/', views.ClassSubjectCreateAPIView.as_view(), name='add-class-subject'),
    path('class-subjects/<int:pk>/', views.ClassSubjectRetrieveUpdateDestroyAPIView.as_view(), name='class-subject-detail'),
    path('api/student-list/', views.StudentsBySectionListAPIView.as_view(), name='students_by_section'),
]
