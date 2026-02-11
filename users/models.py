from django.db import models
from django.contrib.auth.models import User

# users/models.py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    current_price_id = models.CharField(
        max_length=100,
        blank=True,
        default="",   # ← ★これを追加
    )
