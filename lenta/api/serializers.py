from rest_framework import serializers

from categories.models import Categories
from forecast.models import Forecast, ForecastSales, SalesUnits
from sales.models import FactSales, Sales
from shops.models import Shops


class ShopsSerializer(serializers.ModelSerializer):
    """ Сериализатор для магазина. """
    class Meta:
        model = Shops
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    """ Сериализатор для товара. """
    class Meta:
        model = Categories
        fields = '__all__'


class SalesUnitsSerializer(serializers.ModelSerializer):
    """ Сериализатор для даты отсчета. """
    class Meta:
        model = SalesUnits
        fields = '__all__'


class ForecastSalesSerializer(serializers.ModelSerializer):
    """ Сериализатор для даты отсчета. """
    class Meta:
        model = ForecastSales
        fields = '__all__'

class ForecastSerializer(serializers.ModelSerializer):
    forecast = serializers.SerializerMethodField()

    def get_forecast(self, obj):
        if obj.forecast.count() > 1:
            sales_units = obj.forecast.all()
            forecast_data = {}
            for unit in sales_units:
                forecast_data[unit.future_date.strftime('%Y-%m-%d')] = unit.units
            return forecast_data
        return None
# class ForecastSerializer(serializers.ModelSerializer):
#     """ Сериализатор для предсказания. """
#     forecast = serializers.SerializerMethodField()

#     def get_forecast(self, obj):
#         sales_units = SalesUnits.objects.filter(id__in=obj.forecast.values_list('id', flat=True))
#         forecast_data = {}
#         for unit in sales_units:
#             forecast_data[unit.future_date.strftime('%Y-%m-%d')] = unit.units
#         return forecast_data

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')

class ForecastDataSerializer(serializers.Serializer):
    store = serializers.CharField()
    sku = serializers.CharField()
    forecast_date = serializers.DateField()
    forecast = serializers.DictField()


# class FactSalesSerialiser(serializers.ModelSerializer):
#     """ Сериализатор для фактической продажи """
#     class Meta:
#         model = FactSales
#         fields = ('date', 'sales_type', 'sales_units',
#                   'sales_units_promo', 'sales_rub', 'sales_run_promo')


class SalesSerializer(serializers.ModelSerializer):
    """ Сериализатор для продажи. """
    store = ShopsSerializer()
    sku = CategoriesSerializer()
    # fact = FactSalesSerialiser()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['store'] = data['store']['store']  # Получите значение 'store' из вложенного сериализатора
        data['sku'] = data['sku']['sku']

        # data['fact'] = [{'date': fact_instance['date'],
        #                  'sales_type': fact_instance['sales_type'],
        #                  'sales_units': fact_instance['sales_units'],
        #                  'sales_units_promo': fact_instance['sales_units_promo'],
        #                  'sales_rub': fact_instance['sales_rub'],
        #                  'sales_run_promo': fact_instance['sales_run_promo']}
        #                 for fact_instance in data['fact']]
        
        data['fact'] = [{'date': fact_instance.date,
                         'sales_type': fact_instance.sales_type,
                         'sales_units': fact_instance.sales_units,
                         'sales_units_promo': fact_instance.sales_units_promo,
                         'sales_rub': fact_instance.sales_rub,
                         'sales_run_promo': fact_instance.sales_run_promo}
                        for fact_instance in instance.fact.all()]
        return data
    
    
    # def to_representation(self, instance):
    #     # Переопределение представления для вложенного сериализатора
    #     return instance.store


    class Meta:
        model = Sales
        fields = ('store', 'sku', 'fact')
