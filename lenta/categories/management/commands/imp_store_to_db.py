from django.core.management.base import BaseCommand
import pandas as pd

from shops.models import Shops


class Command(BaseCommand):
    help = 'Import SKU data from CSV to the database'

    def handle(self, *args, **kwargs):
        csv_file_path = 'data/st_df.csv'
        data = pd.read_csv(csv_file_path)

        data_dict = data.to_dict(orient='records')

        for item in data_dict:
            Shops.objects.create(
                store=item['st_id'],
                city=item['st_city_id'],
                division=item['st_division_code'],
                type_format=item['st_type_format_id'],
                loc=item['st_type_loc_id'],
                size=item['st_type_size_id'],
                is_active=item['st_is_active']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported Store data'))