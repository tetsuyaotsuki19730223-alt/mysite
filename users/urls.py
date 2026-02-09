from django.urls import path
from .views import create_checkout_session

urlpatterns = [
    path("subscribe/", create_checkout_session, name="subscribe"),
]
