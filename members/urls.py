from django.urls import path
from .views import MemberOnlyView

urlpatterns = [
    path('', MemberOnlyView.as_view(), name='member_home'),
]
