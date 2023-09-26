# Generated by Django 4.2.5 on 2023-09-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sales_rub',
            field=models.FloatField(help_text='продажи без признака промо в РУБ', verbose_name='sales_rub'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_run_promo',
            field=models.FloatField(help_text='продажи с признаком промо в РУБ', verbose_name='sales_run_promo'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_units',
            field=models.IntegerField(help_text='число проданных товаров без признака промо', verbose_name='sales_units'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='sales_units_promo',
            field=models.IntegerField(help_text='число проданных товаров с признаком промо', verbose_name='sales_units'),
        ),
    ]