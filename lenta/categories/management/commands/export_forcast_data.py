import csv
from django.core.management.base import BaseCommand
from forecast.models import Forecast, ForecastSales, SalesUnits

class Command(BaseCommand):
    help = 'Экспорт данных в CSV файл'

    def handle(self, *args, **options):
        file_path = 'forecast_data.csv'  # Укажите путь к файлу

        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Заголовки CSV-файла
            writer.writerow(['Store', 'SKU', 'Forecast Date', 'Future Date', 'Units'])

            # Итерация по объектам модели Forecast
            for forecast in Forecast.objects.all():
                store = forecast.store.store
                forecast_date = forecast.forecast_date

                # Итерация по связанным объектам ForecastSales
                for forecast_sale in forecast.forecast.all():
                    sku = forecast_sale.sku.sku

                    # Итерация по связанным объектам SalesUnits
                    for sales_unit in forecast_sale.sales_units.all():
                        future_date = sales_unit.future_date
                        units = sales_unit.units

                        # Запись данных в CSV-файл
                        writer.writerow([store, sku, forecast_date, future_date, units])

        self.stdout.write(self.style.SUCCESS(f'Экспорт завершен. Файл: {file_path}'))