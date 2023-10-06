from django.core.management.base import BaseCommand
import pandas as pd

from categories.models import Categories


class Command(BaseCommand):
    help = 'Import SKU data from CSV to the database'

    def handle(self, *args, **kwargs):
        csv_file_path = 'data/pr_df.csv'
        data = pd.read_csv(csv_file_path)

        data_dict = data.to_dict(orient='records')

        for item in data_dict:
            Categories.objects.create(
                sku=item['pr_sku_id'],
                group=item['pr_group_id'],
                category=item['pr_cat_id'],
                subcategory=item['pr_subcat_id'],
                uom=item['pr_uom_id']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported SKU data'))


# import pandas as pd
# from categories.models import Categories

# # Загрузка данных из CSV
# csv_file_path = 'data/pr_df.csv'
# data = pd.read_csv(csv_file_path)

# # Преобразование DataFrame в список словарей
# data_dict = data.to_dict(orient='records')

# # Создание объектов модели Django
# for item in data_dict:
#     Categories.objects.create(
#         sku=item['pr_sku_id'],
#         group=item['pr_group_id'],
#         category=item['pr_cat_id'],
#         subcategory=item['pr_subcat_id'],
#         uom=item['pr_uom_id']
#     )