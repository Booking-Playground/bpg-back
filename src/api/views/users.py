from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from src.api.serializers.playground import UserReadSerializer


User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
