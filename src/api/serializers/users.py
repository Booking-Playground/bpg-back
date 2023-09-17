from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    """
    Serializer for Registration users.
    """

    username = None
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    phone = PhoneNumberField(
        required=True,
        max_length=16,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["phone"] = self.validated_data.get("phone", "")
        data_dict["first_name"] = self.validated_data.get("first_name", "")
        data_dict["last_name"] = self.validated_data.get("last_name", "")
        return data_dict


class CustomLoginSerializer(LoginSerializer):
    """Only email anp password."""

    username = None


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """User model w/o password."""

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
        )
        read_only_fields = ("email",)
