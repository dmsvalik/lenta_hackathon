# from django.shortcuts import render
# from rest_framework import filters, status, viewsets
from rest_framework.viewsets import ModelViewSet
from categories.models import Categories
from forecast.models import Forecast, ForecastDay
from api.serializer import CategoriesSerializer, ForecastDaySerializer, ForecastSerializer, SalesSerializer, ShopsSerializer
from shops.models import Shops
from sales.models import Sales


class CategoriesViewSet(ModelViewSet):
    """ Список товаров. """
    queryset = Categories.objects.all()

    def get_serializer_class(self):
        return CategoriesSerializer


class ForecastViewSet(ModelViewSet):
    """ Список предсказаний. """
    queryset = Forecast.objects.all()

    def get_serializer_class(self):
        return ForecastSerializer


class ForecastDayViewSet(ModelViewSet):
    """ Список даты предсказания. """
    queryset = ForecastDay.objects.all()

    def get_serializer_class(self):
        return ForecastDaySerializer


class SalesViewSet(ModelViewSet):
    """ Список покупок. """
    queryset = Sales.objects.all()

    def get_serializer_class(self):
        return SalesSerializer


class ShopsViewSet(ModelViewSet):
    """ Список магазинов. """
    queryset = Shops.objects.all()

    def get_serializer_class(self):
        return ShopsSerializer
