from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import *

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoriesViewSet, basename='categories')
router_v1.register('forecast', ForecastViewSet, basename='forecast')
router_v1.register('sales', SalesViewSet, basename='sales')
router_v1.register('shops', ShopsViewSet, basename='shops')


urlpatterns = [
    path('', include(router_v1.urls)),
]