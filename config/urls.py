from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def healthcheck(request):
    return HttpResponse("Django is alive on Render")

urlpatterns = [
    #path("health/", healthcheck),   # ← 追加（最重要）
    path("admin/", admin.site.urls),
    #path("", include("blog.urls")),
    #path("", include("users.urls")),
]
