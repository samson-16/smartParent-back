from rest_framework import serializers
from .models import ChatMessage
from core_app.serializers import UserSerializer
class ChatMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id' , 'sender', 'receiver' , 'message']

class ListChatMessagesSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model = ChatMessage
        fields = ['id' , 'sender', 'receiver' , 'message']