from django.db import models

# Create your models here.
from posts.models import Post



class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.name}"



class PostHashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="hashtags")
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"#{self.hashtag.name} in Post {self.post.id}"


"""
✅ Best Practices:
Uses a separate model for hashtags for better querying.
Enables many-to-many relationship with posts.
"""