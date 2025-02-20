

from interactions.models import Comment, Follow
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from django.apps import apps  



#@receiver(post_save, sender=Like)
@receiver(post_save, sender=apps.get_model("interactions", "Like"))
def notify_like(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.author,
            sender=instance.user,
            type="like",
            message=f"{instance.user.username} liked your post."
        )


@receiver(post_save, sender=Comment)
def notify_comment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.post.author,
            sender=instance.user,
            type="comment",
            message=f"{instance.user.username} commented on your post."
        )


@receiver(post_save, sender=Follow)
def notify_follow(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.following,
            sender=instance.follower,
            type="follow",
            message=f"{instance.follower.username} started following you."
        )


#Generate Notifications Automatically.