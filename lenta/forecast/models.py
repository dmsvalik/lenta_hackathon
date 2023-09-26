from django.db import models
from shops.models import Shops
from categories.models import Categories

class ForecastDay(models.Model):
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
    forecast_date = models.DateField(
        help_text='Дата отсечки'
    )
    forecast = models.ForeignKey(
        ForecastDay,
        on_delete=models.CASCADE,
        related_name='forecast',
        verbose_name='прогноз',
        help_text='Прогноз'
    )
        
    class Meta:
        ordering = ('store', 'sku', 'forecast')
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогноз'

    def __str__(self):
        return self.store
