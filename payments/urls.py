from django.urls import path
from payments.views import subscribe, stripe_webhook

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("webhook/", stripe_webhook, name="stripe_webhook"),
]
