

# Create your models here.
from django.contrib.auth import get_user_model
from posts.models import Post
from django.db import models

User = get_user_model()  



class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")  # Prevent duplicate follows

    def __str__(self):
        return f"{self.follower} follows {self.following}"

"""
✅ Best Practices:
Uses a self-referential ForeignKey for User to establish a follow system.
Ensures a user cannot follow the same person twice with unique_together.
"""



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.post.id}"

"""
✅ Best Practices:
Prevents duplicate likes with unique_together.
Allows multiple comments per post.
Keeps track of timestamps.
"""