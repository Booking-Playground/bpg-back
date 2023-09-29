from rest_framework import serializers

from booking.models import Booking, SettingsBooking
from api.serializers.playground import SmallPlaygroundSerializer
from api.serializers.users import CustomUserDetailsSerializer


class SettingsBookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "booking_enable",
            "confirmation_required",
            "disable_weekend",
            "available_booking_months",
            "start_time",
            "end_time",
            "period_of_each_booking",
        )
        model = SettingsBooking


class ReadBookingSerializer(serializers.ModelSerializer):
    """Read information booking of sports grounds."""

    user = CustomUserDetailsSerializer(
        many=False,
        read_only=True,
    )
    status = serializers.SerializerMethodField(method_name="get_status")
    playground = SmallPlaygroundSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        fields = (
            "id",
            "status",
            "user",
            "playground",
            "date",
            "time",
        )
        model = Booking

    def get_status(self, obj):
        return obj.get_status_display()


class WriteBookingSerializer(serializers.ModelSerializer):
    """Write information booking of sports grounds."""

    user = CustomUserDetailsSerializer(
        many=False,
        read_only=True,
    )
    playground = SmallPlaygroundSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        fields = (
            "id",
            "playground",
            "user",
            "date",
            "time",
        )
        read_only_fields = ("id",)
        model = Booking
