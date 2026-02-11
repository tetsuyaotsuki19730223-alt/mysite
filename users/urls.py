from django.urls import path
from .views import subscribe, success, cancel, stripe_webhook

urlpatterns = [
    path("subscribe/", subscribe),
    path("success/", success),
    path("cancel/", cancel),
    path("stripe/webhook/", stripe_webhook),
]
