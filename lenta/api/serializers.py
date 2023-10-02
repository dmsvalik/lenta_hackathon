from rest_framework import serializers

from categories.models import Categories
from forecast.models import Forecast, SalesUnits
from sales.models import Sales
from shops.models import Shops
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')


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

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'forecast_date', 'forecast')

class ForecastDataSerializer(serializers.Serializer):
    store = serializers.CharField()
    sku = serializers.CharField()
    forecast_date = serializers.DateField()
    forecast = serializers.DictField()


class SalesSerializer(serializers.ModelSerializer):
    """ Сериализатор для продажи. """
    class Meta:
        model = Sales
        fields = '__all__'


class ShopsSerializer(serializers.ModelSerializer):
    """ Сериализатор для магазина. """
    class Meta:
        model = Shops
        fields = '__all__'
