from django.urls import path
from .views import subscribe, success, cancel, stripe_webhook

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
