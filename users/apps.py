from django.apps import AppConfig
import os

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        if os.environ.get("CREATE_SUPERUSER") == "true":
            username = "admin"
            password = "admin123"

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email="admin@example.com",
                    password=password
                )
                print("🔥 SUPERUSER CREATED")