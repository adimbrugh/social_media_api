

from .models import Follow, Like, Comment
from rest_framework import serializers



class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source="follower.username")
    following = serializers.ReadOnlyField(source="following.username")

    class Meta:
        model = Follow
        fields = ["id", "follower", "following", "created_at"]



class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]

        

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at"]
