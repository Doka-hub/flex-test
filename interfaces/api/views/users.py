from rest_framework import generics

from apps.users.models import User
from interfaces.api.serializers.users import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
