from django.urls import path
from .views import subscribe, stripe_webhook

urlpatterns = [
    path("subscribe/", subscribe),
]
