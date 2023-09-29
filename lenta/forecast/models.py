from django.db import models
from shops.models import Shops
from categories.models import Categories

class SalesUnits(models.Model):
    """ Модель прогноза продаж будущих дней"""
    future_date = models.DateField(
        help_text='Дата будущих продаж'
    )
    units = models.IntegerField(
        verbose_name='units',
        help_text='Колличество позиций'
    )


class Forecast(models.Model):
    """ Модель прогноза продаж. """
    store = models.ManyToManyField(
        Shops,
        # on_delete=models.CASCADE,
        # related_name='store',
        verbose_name='торговый центр',
        help_text='Выберите торговый центр'
    )
    sku = models.ManyToManyField(
        Categories,
        # on_delete=models.CASCADE,
        # related_name='sku',
        verbose_name='товар',
        help_text='Выберите товар'
    )
    forecast_date = models.DateField(
        help_text='Дата отсечки'
    )
    forecast = models.ManyToManyField(
        SalesUnits,
        # on_delete=models.CASCADE,
        related_name='forecast',
        verbose_name='прогноз',
        help_text='Прогноз'
    )

    def __str__(self):
        return f"{self.store} - {self.forecast_date.strftime('%Y, %B %d')}"
