from django.urls import path
from .views import create_checkout_session, stripe_webhook

urlpatterns = [
    path("subscribe/", create_checkout_session, name="subscribe"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
