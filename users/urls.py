from django.urls import path
from .views import stripe_webhook, subscribe

urlpatterns = [
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
    path("subscribe/", subscribe, name="subscribe"),
]
