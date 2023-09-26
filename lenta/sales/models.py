from django.db import models
from shops.models import Shops
from categories.models import Categories

class Sales(models.Model):
    """ Модель Продажа. """
    store = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        # related_name='store',
        verbose_name='торговый центр',
        help_text='Выберите торговый центр'
    )
    sku = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        # related_name='sku',
        verbose_name='товар',
        help_text='Выберите товар'
    )
    date = models.DateField(
        help_text='Время продажи'
    )
    sales_type = models.IntegerField(
        verbose_name='sales_type',
        help_text='тип продажи'
    )
    sales_units = models.IntegerField(
        verbose_name='sales_units',
        help_text='подразделение продажи'
    )
    sales_units_promo = models.IntegerField(
        verbose_name='sales_units',
        help_text='подразделение продажи'
    )
    sales_rub = models.FloatField(
        verbose_name='sales_rub',
        help_text='стоимость продажи'
    )
    sales_run_promo = models.FloatField(
        verbose_name='sales_run_promo',
        help_text='промо продажи'
    )
    
    class Meta:
        ordering = ('store', 'sku', 'date')
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажа'

    def __str__(self):
        return self.store
