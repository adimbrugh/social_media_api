

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FollowViewSet


router = DefaultRouter()
router.register(r"follows", FollowViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
