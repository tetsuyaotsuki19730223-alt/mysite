from users.models import Profile

MONTHLY_PRICE = 1000  # 円（あとで環境変数でもOK）

def get_kpi():
    active_users = Profile.objects.filter(is_subscribed=True).count()
    total_users = Profile.objects.count()

    mrr = active_users * MONTHLY_PRICE

    churn_rate = 0
    if total_users > 0:
        churn_rate = round(
            (total_users - active_users) / total_users * 100, 2
        )

    return {
        "active_users": active_users,
        "total_users": total_users,
        "mrr": mrr,
        "churn_rate": churn_rate,
    }
