from django.urls import path
from .views import post_detail, index

app_name = "blog"

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("", index, name="index"),
]
