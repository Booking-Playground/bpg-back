from rest_framework import serializers

from booking.models import Booking, SettingsBooking
from api.serializers.users import UserReadSerializer


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

    user = UserReadSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        fields = (
            "id",
            "user",
            "playground",
            "date",
            "time",
        )
        model = Booking


class WriteBookingSerializer(serializers.ModelSerializer):
    """Write information booking of sports grounds."""

    user = UserReadSerializer(many=False, read_only=True)

    class Meta:
        fields = (
            "id",
            "user",
            "playground",
            "date",
            "time",
            "approved",
            "created_at",
            "updated_at",
        )
        model = Booking
