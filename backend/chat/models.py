from django.db import models
from core_app.models import User
# Create your models here.

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "receiver")

    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"{self.sender.username} - {self.receiver.username}"
    
    @property
    def sender_profile(self):
        return self.sender
    
    @property
    def receiver_profile(self):
        return self.receiver

