from celery import shared_task

from interfaces.github_api import fetch_github_data
from .models import Subscription


@shared_task
def update_subscriptions_task():
    subs = Subscription.objects.all()
    for sub in subs:
        try:
            data = fetch_github_data(sub.github_username)
            sub.public_repos = data["public_repos"]
            sub.languages = ",".join(data["languages"])
            sub.latest_repos = ",".join(data["latest_repos"])
            sub.last_commit = data["last_commit"]
            sub.save(
                update_fields=[
                    'public_repos',
                    'languages',
                    'latest_repos',
                    'last_commit',
                ]
            )
        except Exception as e:
            print(f"Error updating {sub.github_username}: {e}")
