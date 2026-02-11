from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe


def subscribe(request):
    return HttpResponse("SUBSCRIBE OK")


@csrf_exempt
def stripe_webhook(request):
    return HttpResponse("WEBHOOK OK")
