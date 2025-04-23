from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.subscriptions.models import Subscription
from apps.subscriptions.tasks import update_subscriptions_task
from interfaces.api.serializers.subscriptions import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='cron/update')
    def trigger_update(self, request):
        update_subscriptions_task.delay()
        return Response({"msg": "Обновление подписок запущено"}, status=status.HTTP_202_ACCEPTED)
