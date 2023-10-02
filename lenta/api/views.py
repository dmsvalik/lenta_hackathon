# from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from categories.models import Categories
from forecast.models import Forecast, SalesUnits
from api.serializers import (
    CategoriesSerializer,
    SalesUnitsSerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopsSerializer
)
from shops.models import Shops
from sales.models import Sales


class BaseAPIVIew(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {'data': serializer.data}
        return Response(data)


class CategoriesAPIView(BaseAPIVIew):
    """ Список товаров. """
    queryset = Categories.objects.all()

    def get_serializer_class(self):
        return CategoriesSerializer


class ForecastAPIView(BaseAPIVIew):
    """ Список предсказаний. """
    queryset = Forecast.objects.all()

    def get_serializer_class(self):
        return ForecastSerializer


class ForecastDataView(APIView):
    def get(self, request):
        queryset = Forecast.objects.all()
        serializer = ForecastSerializer(queryset, many=True)
        data = {'data': serializer.data}
        return Response(data)

    def post(self, request, format=None):
        serializer = SalesUnitsSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            store = data['store']
            sku = data['sku']
            forecast_date = data['forecast_date']
            forecast = data['forecast']

            # Создайте или обновите запись в модели Forecast
            forecast_obj, created = Forecast.objects.get_or_create(
                store=store,
                sku=sku,
                forecast_date=forecast_date,
                forecast=forecast
            )
            forecast_obj.forecast = forecast
            forecast_obj.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalesAPIView(BaseAPIVIew):
    """ Список покупок. """
    queryset = Sales.objects.all()

    def get_serializer_class(self):
        return SalesSerializer


class ShopsAPIView(BaseAPIVIew):
    """ Список магазинов. """
    queryset = Shops.objects.all()

    def get_serializer_class(self):
        return ShopsSerializer
