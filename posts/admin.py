from django.contrib import admin

# Register your models here.
from .models import Post  # ✅ Make sure the import is correct

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "author", "created_at")
