from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def has_active_subscription(self) -> bool:
        """
        有料会員かどうかを返す。
        Profile が無い場合でも False を返す（安全）
        """
        profile = getattr(self, "profile", None)
        if not profile:
            return False
        return bool(profile.is_subscribed)
