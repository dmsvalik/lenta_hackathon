# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from categories.models import Categories
from forecast.models import Forecast, SalesUnits
from api.serializer import CategoriesSerializer, ForecastDataSerializer, ForecastSerializer, SalesSerializer, SalesUnitsSerializer, ShopsSerializer
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


class SalesUnitsViewSet(ModelViewSet):
    """ Список предсказаний. """
    queryset = SalesUnits.objects.all()

    def get_serializer_class(self):
        return SalesUnitsSerializer


class ForecastDataView(APIView):
    def post(self, request, format=None):
        serializer = ForecastDataSerializer(data=request.data)

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

# @api_view(['POST'])
# def create_forecast(request):
#     if request.method == 'POST':
#         store = request.data.get('store')
#         forecast_date = request.data.get('forecast_date')
#         sku = request.data.get('sku')
#         sales_units_data = request.data.get('sales_units')

#         # Создайте объекты модели и сохраните их
#         forecast = Forecast.objects.create(store=store, forecast_date=forecast_date, sku=sku)
#         for date, units in sales_units_data.items():
#             SalesUnits.objects.create(date=date, units=units, forecast=forecast)

#         return Response("Forecast created successfully", status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def get_forecast(request):
#     if request.method == 'GET':
#         store = request.query_params.get('store')
#         sku = request.query_params.get('sku')
#         forecast_date = request.query_params.get('forecast_date')

#         # Выполните фильтрацию по параметрам и получите соответствующие объекты
#         forecasts = Forecast.objects.filter(store=store, sku=sku, forecast_date=forecast_date)
#         serializer = ForecastSerializer(forecasts, many=True)
#         return Response({"data": serializer.data})


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
