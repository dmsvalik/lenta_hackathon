# Generated by Django 4.2.5 on 2023-09-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('future_date', models.DateField(help_text='Дата будущих продаж')),
                ('units', models.IntegerField(help_text='Колличество позиций', verbose_name='units')),
            ],
        ),
        migrations.AlterModelOptions(
            name='forecast',
            options={},
        ),
        migrations.RemoveField(
            model_name='forecast',
            name='forecast',
        ),
        migrations.DeleteModel(
            name='ForecastDay',
        ),
        migrations.AddField(
            model_name='forecast',
            name='forecast',
            field=models.ManyToManyField(help_text='Прогноз', related_name='forecast', to='forecast.salesunits', verbose_name='прогноз'),
        ),
    ]