from django.urls import path
from .views import subscribe, stripe_webhook
from django.http import HttpResponse

urlpatterns = [
    path("subscribe/", subscribe),
    path("stripe/webhook/", stripe_webhook),
    path("success/", lambda r: HttpResponse("SUCCESS")),
    path("cancel/", lambda r: HttpResponse("CANCEL")),
]
