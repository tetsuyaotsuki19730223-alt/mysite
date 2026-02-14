from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model("auth", "User")

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )

class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_profile_stripe_customer_id_and_more"),  # ←最後の番号に合わせる
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
