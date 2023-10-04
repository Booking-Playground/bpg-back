from django.db import models


class BookingStatusOptions(models.IntegerChoices):
    CREATED = 0, "Создан"
    CONFIRMED = 1, "Подтвержден"
    CANCELLED = 2, "Отменен"
    FINISHED = 3, "Завершен"
