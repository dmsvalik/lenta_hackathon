from rest_framework import serializers

from categories.models import Categories
from forecast.models import Forecast, ForecastDay
from sales.models import Sales
from shops.models import Shops


class CategoriesSerializer(serializers.ModelSerializer):
    """ Сериализатор для товара. """
    class Meta:
        model = Categories
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    """ Сериализатор для предсказания. """
    class Meta:
        model = Forecast
        fields = '__all__'


class ForecastDaySerializer(serializers.ModelSerializer):
    """ Сериализатор для даты отсчета. """
    class Meta:
        model = ForecastDay
        fields = '__all__'


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
