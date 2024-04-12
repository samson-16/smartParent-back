# messaging/views.py
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ChatMessage
from .serializers import ChatMessageCreateSerializer, ListChatMessagesSerializer
from rest_framework.permissions import AllowAny

class ChatMessageListView(ListAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ListChatMessagesSerializer
    permission_classes = [AllowAny] 

class ChatMessageCreateView(CreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageCreateSerializer
    permission_classes = [AllowAny] 
