from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path("health/", health),
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
]
