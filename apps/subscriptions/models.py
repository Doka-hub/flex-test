from django.conf import settings
from django.db import models


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    github_username = models.CharField(max_length=255)
    public_repos = models.IntegerField(default=0)
    languages = models.TextField(blank=True)
    latest_repos = models.TextField(blank=True)
    last_commit = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
