from django.urls import path
from .views import ChatMessageCreateView, ChatMessageListView

urlpatterns = [
    path('send-message/', ChatMessageCreateView.as_view(), name='send-message'),
    path('messages/', ChatMessageListView.as_view(), name='list-message'),
]

