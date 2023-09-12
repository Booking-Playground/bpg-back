from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema

from api.serializers.playground import UserReadSerializer


User = get_user_model()


@extend_schema(tags=["Users"])
class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
