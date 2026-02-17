from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    current_price_id = models.CharField(max_length=200, blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=200, blank=True, null=True)

    blog_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner"
    )

    def __str__(self):
        return self.user.username