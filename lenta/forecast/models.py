from django.db import models
from shops.models import Shops
from categories.models import Categories


class SalesUnits(models.Model):
    """ Модель будущих дней продаж и колличества"""
    future_date = models.DateField(
        help_text='Дата будущих продаж'
    )
    units = models.IntegerField(
        verbose_name='units',
        help_text='Колличество позиций'
    )


class ForecastSales(models.Model):
    """ Модель зависимости товара и даты будущих продаж"""
    sku = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        # related_name='sku',
        verbose_name='товар',
        help_text='Выберите товар'
    )
    sales_units = models.ManyToManyField(
        SalesUnits,
        # on_delete=models.CASCADE,
        related_name='sales_units',
        verbose_name='будущие продажи',
        help_text='Будущие продажи'
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
    forecast_date = models.DateField(
        help_text='Дата отсечки'
    )
    forecast = models.ManyToManyField(
        ForecastSales,
        # on_delete=models.CASCADE,
        related_name='forecast',
        verbose_name='прогноз',
        help_text='Прогноз'
    )

    def __str__(self):
        unique_skus = set(sale.sku.sku for sale in self.forecast.all())
        skus = ', '.join(unique_skus)
        return f"{self.store} - {skus} - {self.forecast_date.strftime('%Y, %B %d')}"
