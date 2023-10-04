from rest_framework import serializers

from categories.models import Categories
from forecast.models import Forecast, ForecastSales, SalesUnits
from sales.models import FactSales, Sales
from shops.models import Shops
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


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
    sales_units = SalesUnitsSerializer(many=True)
    class Meta:
        model = ForecastSales
        fields = '__all__'


class SalesUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesUnits
        fields = '__all__'

class ForecastSalesSerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source='sku.sku')
    sales_units = SalesUnitsSerializer(many=True)

    class Meta:
        model = ForecastSales
        fields = ('sku', 'sales_units')

class ForecastSerializer(serializers.ModelSerializer):
    forecast = ForecastSalesSerializer(many=True, read_only=True)
    store = serializers.CharField(source='store.store')
    sku = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date', 'forecast')

    def get_sku(self, instance):
        # Динамически получаем sku из первого элемента forecast
        return instance.forecast.first().sku.sku if instance.forecast.exists() else None

    def to_representation(self, instance):
        forecast_data = []
        for forecast_sale in instance.forecast.all():
            for sales_unit in forecast_sale.sales_units.all():
                future_date = str(sales_unit.future_date)
                forecast_data.append({
                    'date': future_date,
                    'units': sales_unit.units
                })

        return {
            "data": [
                {
                    "store": instance.store.store,
                    "sku": self.get_sku(instance),
                    "forecast_date": str(instance.forecast_date),
                    "forecast": {item['date']: item['units'] for item in forecast_data}
                }
            ]
        }


class SalesSerializer(serializers.ModelSerializer):
    """ Сериализатор для продажи. """
    store = ShopsSerializer()
    sku = CategoriesSerializer()
    
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['store'] = data['store']['store']  # Получите значение 'store' из вложенного сериализатора
        data['sku'] = data['sku']['sku']
        data['fact'] = [{'date': fact_instance.date,
                         'sales_type': fact_instance.sales_type,
                         'sales_units': fact_instance.sales_units,
                         'sales_units_promo': fact_instance.sales_units_promo,
                         'sales_rub': fact_instance.sales_rub,
                         'sales_run_promo': fact_instance.sales_run_promo}
                        for fact_instance in instance.fact.all()]
        return data

    class Meta:
        model = Sales
        fields = ('store', 'sku', 'fact')
