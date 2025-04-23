from rest_framework import serializers
import requests


def fetch_github_data(username):
    with requests.Session() as client:
        user = client.get(f"https://api.github.com/users/{username}", timeout=5)
        repos = client.get(
            f"https://api.github.com/users/{username}/repos?sort=pushed&per_page=5",
            timeout=5
        )

        if not user.ok or not repos.ok:
            raise serializers.ValidationError("Ошибка при получении данных из GitHub API")

        repos_data = repos.json()
        return {
            "public_repos": user.json().get("public_repos", 0),
            "latest_repos": [r["name"] for r in repos_data],
            "languages": list({r.get("language") for r in repos_data if r.get("language")}),
            "last_commit": repos_data[0]["pushed_at"] if repos_data else None
        }
