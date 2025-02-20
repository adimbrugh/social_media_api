

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from interactions.views import FollowViewSet, LikeViewSet, CommentViewSet
from notifications.views import NotificationViewSet
from posts.views import PostViewSet, trending_posts
from rest_framework.routers import DefaultRouter
from messaging.views import MessageViewSet
from django.urls import path, include
from users.views import UserViewSet


router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename='notifications')
router.register(r"messages", MessageViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"follows", FollowViewSet)
router.register(r"likes", LikeViewSet)
router.register(r"posts", PostViewSet)
router.register(r"users", UserViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("trending/", trending_posts, name="trending-posts"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]