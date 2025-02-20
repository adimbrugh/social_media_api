

from rest_framework import serializers
from .models import Message



class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source="sender.username")
    receiver = serializers.ReadOnlyField(source="receiver.username")

    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "text", "timestamp", "is_read"]
