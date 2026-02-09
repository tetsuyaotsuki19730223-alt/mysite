from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("users urls OK")

urlpatterns = [
    path("subscribe/", test),
]
