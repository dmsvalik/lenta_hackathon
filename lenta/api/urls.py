# from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesViewSet,
    ForecastViewSet,
    SalesViewSet,
    ShopsViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()


urlpatterns = [
    path('', include(router_v1.urls)),
    path('forecast/', ForecastViewSet.as_view({'get': 'list', 'post': 'create'}), name='forecast'),
    # path('forecast-data/', ForecastData.as_view(), name='forecast-data'),
    path('categories/', CategoriesViewSet.as_view({'get': 'list'}), name='categories'),
    path('sales/', SalesViewSet.as_view({'get': 'list'}), name='sales'),
    path('shops/', ShopsViewSet.as_view({'get': 'list'}), name='shops'),
]
