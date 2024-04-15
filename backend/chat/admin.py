from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'is_read', 'date')
    list_filter = ('sender', 'receiver', 'is_read', 'date')
    search_fields = ('sender__username', 'receiver__username', 'message')