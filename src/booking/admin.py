from django.contrib import admin

from booking.models import Booking, SettingsBooking

admin.site.register(SettingsBooking)
admin.site.register(Booking)
