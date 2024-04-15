# messaging/views.py
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ChatMessage
from .serializers import ChatMessageCreateSerializer, ListChatMessagesSerializer
from rest_framework.permissions import isAuthenticated
from django.db.models import Q

class ChatMessageListView(ListAPIView):
    serializer_class = ListChatMessagesSerializer
    permission_classes = [isAuthenticated]

    def get_queryset(self):
        sender_id = self.request.query_params.get('sender_id')
        receiver_id = self.request.query_params.get('receiver_id')

        if sender_id and receiver_id:
            queryset = ChatMessage.objects.filter(
                (Q(sender_id=sender_id) & Q(receiver_id=receiver_id)) |
                (Q(sender_id=receiver_id) & Q(receiver_id=sender_id))
            ).order_by('-date')
        elif sender_id:
            queryset = ChatMessage.objects.filter(sender_id=sender_id).order_by('-date')
        elif receiver_id:
            queryset = ChatMessage.objects.filter(receiver_id=receiver_id).order_by('-date')
        else:
            queryset = ChatMessage.objects.all()

        return queryset



class ChatMessageCreateView(CreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageCreateSerializer
    permission_classes = [isAuthenticated] 
