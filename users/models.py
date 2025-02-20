

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    cover_photo = models.ImageField(upload_to="cover_photos/", blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoid clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoid clash
        blank=True
    )

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

"""
1️⃣ User Model (Custom User)
We will extend Django's built-in AbstractUser to allow profile customization.
#Best Practices:
Uses AbstractUser for extensibility.
Unique email ensures email-based authentication.
Profile customization fields are included.
"""