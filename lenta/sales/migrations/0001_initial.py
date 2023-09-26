# Generated by Django 4.2.5 on 2023-09-26 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Время продажи')),
                ('sales_type', models.IntegerField(help_text='тип продажи', verbose_name='sales_type')),
                ('sales_units', models.IntegerField(help_text='подразделение продажи', verbose_name='sales_units')),
                ('sales_units_promo', models.IntegerField(help_text='подразделение продажи', verbose_name='sales_units')),
                ('sales_rub', models.FloatField(help_text='стоимость продажи', verbose_name='sales_rub')),
                ('sales_run_promo', models.FloatField(help_text='промо продажи', verbose_name='sales_run_promo')),
                ('sku', models.ForeignKey(help_text='Выберите товар', on_delete=django.db.models.deletion.CASCADE, to='categories.categories', verbose_name='товар')),
                ('store', models.ForeignKey(help_text='Выберите торговый центр', on_delete=django.db.models.deletion.CASCADE, to='shops.shops', verbose_name='торговый центр')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажа',
                'ordering': ('store', 'sku', 'date'),
            },
        ),
    ]
