from django.urls import path
from .views import subscribe, stripe_webhook

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
