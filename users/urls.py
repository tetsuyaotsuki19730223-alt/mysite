from django.urls import path
from .views import (
    subscribe,
    stripe_webhook,
    success,
    cancel,
    premium,
)

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    path("premium/", premium, name="premium"),
]
