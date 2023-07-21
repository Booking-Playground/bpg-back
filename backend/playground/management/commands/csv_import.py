import csv

from django.core.management.base import BaseCommand

from booking_sports.settings import BASE_DIR
from playground.models import Sport, Covering

SUCCESS_IMPORT = 'Импорт файла {} завершен успешно!'
PATH = str(BASE_DIR) + '/static_backend/csv_data/'
FILE_AND_MODEL = {
    Sport: 'sports.csv',
    Covering: 'coverings.csv',
}


def csv_import(csv_data, model):
    data_list = list()
    for values in csv_data:
        data_list.append(model(**values))
    model.objects.bulk_create(
        data_list,
        ignore_conflicts=True,
    )


class Command(BaseCommand):
    """
    Managment command for reads csv file
    and write information in DB.
    """
    def handle(self, *args, **kwargs):
        for model, filename in FILE_AND_MODEL.items():
            with open(PATH + filename, 'r', newline='', encoding='utf-8') as file:
                csv_import(csv.DictReader(file), model)
            self.stdout.write(
                self.style.SUCCESS(SUCCESS_IMPORT.format(filename)))
