# users/decorators.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def subscription_required(view_func):
    @login_required
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        profile = getattr(request.user, "profile", None)

        if not profile or not profile.is_subscribed:
            return redirect("/subscribe/")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
