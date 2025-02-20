
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet, LikeViewSet, CommentViewSet


router = DefaultRouter()
router.register(r"follows", FollowViewSet)
router.register(r"likes", LikeViewSet)
router.register(r"comments", CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
"""