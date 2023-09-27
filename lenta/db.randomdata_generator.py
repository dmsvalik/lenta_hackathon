import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lenta.settings')
import django
django.setup()

from shops.models import Shops
from categories.models import Categories
from sales.models import Sales
import random as rn


for i in range(100):
    Shops.objects.create(
        store=f'Лента {i}',
        city=rn.choice(['СПб', 'Москва', 'Ярославль', 'Екатеринбург']),
        type_format=rn.choice(range(5)),
        division=rn.choice(['СПб', 'Москва', 'Ярославль', 'Екатеринбург']),
        loc=rn.choice(range(100)),
        size=rn.choice(range(100)),
        is_active=1)

    Categories.objects.create(
        sku=rn.choice(range(100)),
        group=rn.choice(['хлеб', 'фрукты', 'вода', 'алкоголь']),
        category=rn.choice(range(100)),
        subcategory=rn.choice(range(100)),
        uom=rn.choice(range(10)))

    Sales.objects.create(
        sales_type=rn.choice(range(10)),
        sales_units=rn.choice(range(100)),
        sales_units_promo=rn.choice(range(100)),
        sales_rub=rn.choice(range(100)),
        sales_run_promo=rn.choice(range(100)),
        store=rn.choice(Shops.objects.all()),
        sku=rn.choice(Categories.objects.all())
    )
