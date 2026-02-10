from django.urls import path
from .views import subscribe, success, cancel

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
]
