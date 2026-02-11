from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_subscribed = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=255, blank=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True)
    current_price_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
