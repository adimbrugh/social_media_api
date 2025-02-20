from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    # Now, notifications are automatically created when users like, comment, or follow! 🚀.
    def ready(self):
        import notifications.signals
