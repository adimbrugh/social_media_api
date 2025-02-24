

# Create your views here.
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import viewsets
from django.shortcuts import render

User = get_user_model()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
