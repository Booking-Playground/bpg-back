from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


class UserRegSerializer(UserCreateSerializer):
    """
    Serializer for Registration users.
    True hashing password.
    """

    class Meta:
        model = User
        fields = (
            "email",
            "phone",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {"password": {"write_only": True}}


class UserReadSerializer(UserSerializer):
    """
    Serializer for read users in other serializer.
    """

    class Meta:
        fields = (
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
        )
        model = User
