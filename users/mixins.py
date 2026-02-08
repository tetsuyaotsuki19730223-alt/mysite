from django.shortcuts import redirect

class SubscriptionRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.profile.is_subscribed:
            return redirect("/payments/subscribe/")
        return super().dispatch(request, *args, **kwargs)
