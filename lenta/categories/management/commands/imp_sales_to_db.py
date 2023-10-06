import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand
from shops.models import Shops
from categories.models import Categories
from sales.models import Sales, FactSales


class Command(BaseCommand):
    help = 'Load data from CSV into Sales and FactSales models'

    def handle(self, *args, **kwargs):
        file_path = 'data/sales_df_train.csv'  # Укажите путь к вашему CSV-файлу
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            # Проверяем, существуют ли магазин и товар
            store = row['st_id']
            sku = row['pr_sku_id']
            store = Shops.objects.get(store=store)
            sku = Categories.objects.get(sku=sku)

            # Создаем объекты FactSales
            fact_sales = FactSales.objects.create(
                date=datetime.strptime(row['date'], '%Y-%m-%d').date(),
                sales_type=row['pr_sales_type_id'],
                sales_units=row['pr_sales_in_units'],
                sales_units_promo=row['pr_promo_sales_in_units'],
                sales_rub=row['pr_sales_in_rub'],
                sales_run_promo=row['pr_promo_sales_in_rub']
            )

            # Связываем магазин, товар и факт продажи
            sale = Sales.objects.create(store=store, sku=sku)
            sale.fact.add(fact_sales)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
