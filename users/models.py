from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    is_subscribed = models.BooleanField(
        "有料会員",
        default=False
    )

    stripe_customer_id = models.CharField(
        "Stripe顧客ID",
        max_length=255,
        blank=True,
        null=True
    )

    stripe_subscription_id = models.CharField(
        "StripeサブスクリプションID",
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile({self.user})"
