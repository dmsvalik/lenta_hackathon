from django.db import models

class Categories(models.Model):
    '''Модель товара'''
    sku = models.CharField(
        max_length=255,
        verbose_name='sku',
        help_text='Название товара'
    )
    group = models.CharField(
        max_length=255,
        verbose_name='group',
        help_text='Группа товара'
    )
    category = models.CharField(
        max_length=255,
        # verbose_name='category',
        help_text='Категория товара'
    )
    subcategory = models.CharField(
        max_length=255,
        verbose_name='subcategory',
        help_text='Подкатегория товара'
    )
    uom = models.IntegerField(
        verbose_name='uom',
        help_text='Единица измерения товара'
    )
