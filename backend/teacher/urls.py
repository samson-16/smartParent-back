from django.urls import path
from .views import ExamResultListCreate, ExamResultRetrieveUpdateDestroy,AssignmentListCreate, AssignmentRetrieveUpdateDestroy


urlpatterns = [
    path('exam-results/', ExamResultListCreate.as_view(), name='examresult-list-create'),
    path('exam-results/<int:pk>/', ExamResultRetrieveUpdateDestroy.as_view(), name='examresult-retrieve-update-destroy'),
    path('assignments/', AssignmentListCreate.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentRetrieveUpdateDestroy.as_view(), name='assignment-retrieve-update-destroy'),
]
