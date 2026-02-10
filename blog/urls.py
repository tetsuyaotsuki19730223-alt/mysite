from django.urls import path
from .views import premium_article

urlpatterns = [
    path("premium/", premium_article, name="premium"),
]
