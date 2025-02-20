from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model  # ✅ Correct import

User = get_user_model()  # ✅ Get the user model dynamically


# Create your models here.
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