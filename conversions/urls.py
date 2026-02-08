from django.urls import path
from .views import log_cta_and_redirect

app_name = "conversions"

urlpatterns = [
    path("cta/<int:post_id>/", log_cta_and_redirect, name="log_cta"),
]
