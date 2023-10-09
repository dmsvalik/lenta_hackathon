from django.db import models


class Shops(models.Model):
    """ Модель магазина """
    # id = models.CharField(primary_key=True, max_length=32)
    store = models.CharField(
        max_length=255,
        # verbose_name='store',
        help_text='Название магазина'
    )
    city = models.CharField(
        max_length=255,
        verbose_name='city',
        help_text='Город'
    )
    division = models.CharField(
        max_length=255,
        verbose_name='division',
        help_text='Дивизион'
    )
    type_format = models.IntegerField(
        verbose_name='type_format',
        help_text='Формат магазина'
    )
    loc = models.IntegerField(
        verbose_name='loc',
        help_text='Локация магазина'
    )
    size = models.IntegerField(
        verbose_name='size',
        help_text='Размер магазина'
    )
    is_active = models.IntegerField(
        verbose_name='is_active',
        help_text='флаг активного магазина на данный момент'
    )

    def __str__(self):
        return self.store
