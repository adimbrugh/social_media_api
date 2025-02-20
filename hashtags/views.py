from django.shortcuts import render

# Create your views here.
from django.utils.timezone import timedelta, now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.serializers import PostSerializer
from django.utils import timezone
from posts.models import Post



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