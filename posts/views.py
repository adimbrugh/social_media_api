

# Create your views here.
from rest_framework import viewsets, permissions
from django.utils.timezone import now, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from django.shortcuts import render
from django.utils import timezone
from .models import Post



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



@api_view(["GET"])
def trending_posts(request):
    last_24_hours = timezone.now() - timedelta(hours=24)
    trending = Post.objects.filter(created_at__gte=last_24_hours).order_by("-likes")
    serializer = PostSerializer(trending, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def trending_posts(request):
    last_24_hours = now() - timedelta(hours=24)
    trending = Post.objects.filter(created_at__gte=last_24_hours).order_by("-engagement_score")
    serializer = PostSerializer(trending, many=True)
    return Response(serializer.data)
