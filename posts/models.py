

# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db import models

User = get_user_model()



class PostManager(models.Manager):
    def trending(self, time_range="7 days"):
        """Return trending posts based on likes in a given time range."""
        return self.annotate(like_count=Count("likes")).order_by("-like_count")
    


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    media = models.FileField(upload_to="post_media/", blank=True, null=True) # Media field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()  # Custom manager

    #def __str__(self):
       # return f"Post by {self.author.username} on {self.created_at.strftime('%Y-%m-%d')}"

    def engagement_score(self):
        return self.likes.count() + self.comments.count() + self.reposts.count()
    
    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"
    


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
Best Practices:
Uses a separate model for hashtags for better querying.
Enables many-to-many relationship with posts.
"""