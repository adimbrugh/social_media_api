
#social_media_api/
│── manage.py
│── config/                     # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── users/                      # User management app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│── posts/                      # Posts and interactions
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── follows/                    # Follow/Unfollow functionality
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── messages/                   # Direct messaging
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── notifications/              # Notification system
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── hashtags/                   # Hashtags and trending posts
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── media/                      # Media uploads (images/videos)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── common/                     # Shared utilities
│   ├── models.py
│   ├── pagination.py
│   ├── permissions.py
│   ├── utils.py
│── api/
│   ├── __init__.py
│   ├── urls.py
│── requirements.txt
│── .env                        # Environment variables
│── README.md
