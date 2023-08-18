from rest_framework import serializers

from booking.models import SettingsBooking


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
