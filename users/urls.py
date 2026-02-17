from django.urls import path
from .views import (
    subscribe,
    stripe_webhook,
    success,
    cancel,
    premium,
)
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("premium/", views.premium, name="premium"),
    path("stripe/webhook/", views.stripe_webhook),
]
