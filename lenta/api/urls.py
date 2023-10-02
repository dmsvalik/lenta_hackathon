from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesAPIView,
    ForecastDataView,
    SalesAPIView,
    ShopsAPIView,
)

app_name = 'api'

router_v1 = DefaultRouter()
# router_v1.register('forecast', ForecastViewSet, basename='forecast')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('forecast/', ForecastDataView.as_view(), name='forecast-data'),
    path('shops/', ShopsAPIView.as_view()),
    path('sales/', SalesAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view())
    # path('forecast', views.create_forecast),
    # path('forecast', views.get_forecast),
]
