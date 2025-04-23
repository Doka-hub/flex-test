from rest_framework import serializers

from apps.subscriptions.models import Subscription
from interfaces.github_api import fetch_github_data


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'user',
            'github_username',
            'public_repos',
            'languages',
            'latest_repos',
            'last_commit',
            'updated_at',
        )
        read_only_fields = (
            'user',
            'updated_at',
            'public_repos',
            'languages',
            'latest_repos',
            'last_commit',
        )

    def create(self, validated_data):
        github_username = validated_data["github_username"]
        github_data = fetch_github_data(github_username)
        validated_data.update(github_data)
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "github_username" in validated_data:
            github_username = validated_data["github_username"]
            github_data = fetch_github_data(github_username)
            for key, value in github_data.items():
                setattr(instance, key, value)
        return super().update(instance, validated_data)
