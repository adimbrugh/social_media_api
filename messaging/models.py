

# Create your models here.
from posts.models import User
from django.db import models



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

"""
#Best Practices:
Uses self-referential relationships for messaging.
Tracks read/unread status.
Messages are timestamped for order tracking.
"""