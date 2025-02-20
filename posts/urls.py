
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, trending_posts

router = DefaultRouter()
router.register(r"posts", PostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("trending/", trending_posts, name="trending-posts"),
]
"""