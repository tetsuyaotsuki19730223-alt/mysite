from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    LEVEL_CHOICES = [
        ("free", "Free"),
        ("basic", "Basic"),
        ("pro", "Pro"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    blog_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="free"
    )
