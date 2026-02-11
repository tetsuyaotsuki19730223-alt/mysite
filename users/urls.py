from django.urls import path
from .views import subscribe, success, cancel

urlpatterns = [
    path("subscribe/", subscribe),
    path("success/", success),
    path("cancel/", cancel),
]
