from django.contrib import admin

from src.booking.models import Booking, SettingsBooking

admin.site.register(SettingsBooking)
admin.site.register(Booking)
