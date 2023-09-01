from django.contrib.auth import get_user_model
from django.db import models

from src.playground.models import Playground

User = get_user_model()

BOOKING_PERIOD = (
    ("5", "5M"),
    ("10", "10M"),
    ("15", "15M"),
    ("20", "20M"),
    ("25", "25M"),
    ("30", "30M"),
    ("35", "35M"),
    ("40", "40M"),
    ("45", "45M"),
    ("60", "1H"),
    ("75", "1H 15M"),
    ("90", "1H 30M"),
    ("105", "1H 45M"),
    ("120", "2H"),
    ("150", "2H 30M"),
    ("180", "3H"),
)


class SettingsBooking(models.Model):
    playground = models.OneToOneField(
        Playground,
        on_delete=models.CASCADE,
    )
    booking_enable = models.BooleanField(
        default=True,
    )
    confirmation_required = models.BooleanField(
        default=True,
    )
    disable_weekend = models.BooleanField(
        default=True,
    )
    available_booking_months = models.IntegerField(
        default=1,
        help_text="number of months available for booking",
    )

    start_time = models.TimeField(
        default="09:00:00",
    )
    end_time = models.TimeField(
        default="17:00:00",
    )
    period_of_each_booking = models.CharField(
        max_length=3,
        default="30",
        choices=BOOKING_PERIOD,
        help_text="Booking Period.",
    )

    class Meta:
        default_related_name = "settings_playground"

    def __str__(self) -> str:
        return self.playground.playground_name


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    playground = models.ForeignKey(
        Playground,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = "bookings"

    def __str__(self) -> str:
        return f"{self.user} - {self.date} {self.time}"
