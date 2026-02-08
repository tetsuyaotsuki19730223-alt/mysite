from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.http import HttpResponse

def top(request):
    return HttpResponse("🏠 Top Page OK")

def home(request):
    posts = Post.objects.order_by("-id")[:3]  # 最新3件

    profile = None
    if request.user.is_authenticated:
        profile = getattr(request.user, "profile", None)

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "profile": profile,
        },
    )

stripe.api_key = settings.STRIPE_SECRET_KEY

session = stripe.checkout.Session.create(
    mode="subscription",
    payment_method_types=["card"],
    line_items=[{
        "price": settings.STRIPE_PRICE_ID,
        "quantity": 1,
    }],
    success_url="https://your-domain.com/success/",
    cancel_url="https://your-domain.com/cancel/",
)
