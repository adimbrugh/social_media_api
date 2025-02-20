

from rest_framework import serializers
from .models import Notification



class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source="sender.username")

    class Meta:
        model = Notification
        fields = ["id", "sender", "recipient", "type", "message", "created_at", "is_read"]
