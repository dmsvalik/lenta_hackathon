<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-10-09 20:42
=======
# Generated by Django 4.2.5 on 2023-10-04 17:01
>>>>>>> a6ae25c84338e0b77f7b6d4de757176ecd0d7098

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
        ('categories', '0002_alter_categories_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Время продажи')),
                ('sales_type', models.IntegerField(help_text='тип продажи', verbose_name='sales_type')),
                ('sales_units', models.IntegerField(help_text='число проданных товаров без признака промо', verbose_name='sales_units')),
                ('sales_units_promo', models.IntegerField(help_text='число проданных товаров с признаком промо', verbose_name='sales_units_promo')),
                ('sales_rub', models.FloatField(help_text='продажи без признака промо в РУБ', verbose_name='sales_rub')),
                ('sales_run_promo', models.FloatField(help_text='продажи с признаком промо в РУБ', verbose_name='sales_run_promo')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.ManyToManyField(help_text='Фактическая продажа', related_name='fact', to='sales.factsales', verbose_name='фактическая продажа')),
                ('sku', models.ForeignKey(help_text='Выберите товар', on_delete=django.db.models.deletion.CASCADE, to='categories.categories', verbose_name='товар')),
                ('store', models.ForeignKey(help_text='Выберите торговый центр', on_delete=django.db.models.deletion.CASCADE, to='shops.shops', verbose_name='торговый центр')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажа',
            },
        ),
    ]
