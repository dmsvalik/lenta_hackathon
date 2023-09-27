# from django.shortcuts import render
# from rest_framework import filters, status, viewsets
from rest_framework.viewsets import ModelViewSet
from categories.models import Categories
from forecast.models import Forecast, ForecastDay
from api.serializers import (
    CategoriesSerializer,
    ForecastDaySerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopsSerializer
)
from shops.models import Shops
from sales.models import Sales
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class CategoriesAndShopAPIView(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {'data': serializer.data}
        return Response(data)


class CategoriesAPIView(CategoriesAndShopAPIView):
    """ Список товаров. """
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ShopsViewSet(CategoriesAndShopAPIView):
    """ Список магазинов. """
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


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


class SalesViewSet(CategoriesAndShopAPIView):
    """ Список покупок. """
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
