from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MemberOnlyView(LoginRequiredMixin, TemplateView):
    template_name = 'members/index.html'

    # 未ログイン時の遷移先（明示しておくと安心）
    login_url = '/accounts/login/'
