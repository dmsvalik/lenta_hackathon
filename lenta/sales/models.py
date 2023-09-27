from django.db import models
from shops.models import Shops
from categories.models import Categories


class Sales(models.Model):
    """ Модель Продажа. """
    sales_type = models.IntegerField(
        verbose_name='sales_type',
        help_text='тип продажи'
    )
    sales_units = models.IntegerField(
        verbose_name='sales_units',
        help_text='число проданных товаров без признака промо'
    )
    sales_units_promo = models.IntegerField(
        verbose_name='sales_units',
        help_text='число проданных товаров с признаком промо'
    )
    sales_rub = models.FloatField(
        verbose_name='sales_rub',
        help_text='продажи без признака промо в РУБ'
    )
    sales_run_promo = models.FloatField(
        verbose_name='sales_run_promo',
        help_text='продажи с признаком промо в РУБ'
    )
    store = models.ForeignKey(Shops, on_delete=models.CASCADE)
    sku = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажа'
