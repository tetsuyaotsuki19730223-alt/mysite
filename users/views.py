from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def stripe_webhook(request):
    if request.method != "POST":
        return HttpResponse("only POST", status=405)

    payload = request.body
    print("🔥 STRIPE WEBHOOK RECEIVED 🔥")
    print(payload)

    return HttpResponse("ok", status=200)
