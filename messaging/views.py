

# Create your views here.
from .serializers import MessageSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django.shortcuts import render
from .models import Message



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
