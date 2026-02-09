from django.urls import path
from .views import create_checkout_session, stripe_webhook

app_name = "users"

urlpatterns = [
    path("subscribe/", create_checkout_session, name="subscribe"),
    path("subscription/success/", subscription_success, name="subscription_success"),
    path("subscription/cancel/", subscription_cancel, name="subscription_cancel"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
    path("billing/portal/", customer_portal, name="customer_portal"),
]
