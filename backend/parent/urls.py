from django.urls import path
from .views import ParentDashboardAPIView

urlpatterns = [
    path('parent/<int:parent_id>/dashboard/', ParentDashboardAPIView.as_view(), name='parent_dashboard'),
]
