from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_subscribed",
        "stripe_customer_id",
        "stripe_subscription_id",
        "created_at",
    )

    list_filter = (
        "is_subscribed",
    )

    ordering = (
        "-created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
    )
