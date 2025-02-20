

# Create your views here.
from rest_framework import viewsets, permissions
from .serializers import NotificationSerializer
from django.shortcuts import render
from .models import Notification



class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-created_at")
