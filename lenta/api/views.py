from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from categories.models import Categories
from forecast.models import Forecast, ForecastSales, SalesUnits
from api.serializers import (
    CategoriesSerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopsSerializer,
    CustomUserSerializer
)
from users.models import CustomUser
from shops.models import Shops
from sales.models import Sales
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated


class BaseAPIVIew(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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


@authentication_classes([SessionAuthentication, BasicAuthentication])
class ForecastViewSet(ModelViewSet):
    """ Список предсказаний. """
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.get('data')
        print(data)
        forecasts = []

        for item in data:
            store_data = item.get('store')
            forecast_date = item.get('forecast_date')
            forecast_data = item.get('forecast')

            store_instance, _ = Shops.objects.get_or_create(store=store_data.get('store'))
            for forecast_sale_data in forecast_data:
                sku_data = forecast_sale_data.get('sku')
                sales_units_data = forecast_sale_data.get('sales_units')

                sku_instance, _ = Categories.objects.get_or_create(sku=sku_data)
                forecast_sale_instance = ForecastSales.objects.create(sku=sku_instance)

                for sales_unit_data in sales_units_data:
                    future_date = sales_unit_data.get('future_date')
                    units = sales_unit_data.get('units')
                    SalesUnits.objects.create(future_date=future_date, units=units)

                forecast_instance = Forecast.objects.create(store=store_instance, forecast_date=forecast_date)
                forecast_instance.forecast.add(forecast_sale_instance)
                forecasts.append(forecast_instance)

        serializer = self.get_serializer(forecasts, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ForecastCreateAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.get('data')
        for item in data:
            store_name = item.get('store')
            forecast_date = item.get('forecast_date')
            forecast_data = item.get('forecast')
            store = get_object_or_404(Shops, store=store_name)
            forecast, created = Forecast.objects.get_or_create(
                store=store,
                forecast_date=forecast_date
            )
            sku_name = forecast_data.get('sku')
            sku = get_object_or_404(Categories, sku=sku_name)
            forecast_sale, created = ForecastSales.objects.get_or_create(
                sku=sku
            )
            forecast_sale.forecast.add(forecast)
            sales_units_data = forecast_data.get('sales_units')
            for future_date, units in sales_units_data.items():
                sales_units_obj = SalesUnits.objects.create(
                    future_date=future_date,
                    units=units,
                )
                forecast_sale.sales_units.add(sales_units_obj)
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class SalesViewSet(BaseAPIVIew):
    """ Список покупок. """
    queryset = Sales.objects.all()

    def get_serializer_class(self):
        return SalesSerializer


class ShopsAPIView(BaseAPIVIew):
    """ Список магазинов. """
    queryset = Shops.objects.all()

    def get_serializer_class(self):
        return ShopsSerializer


class UsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
