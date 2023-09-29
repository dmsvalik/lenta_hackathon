from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import *

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoriesViewSet, basename='categories')
router_v1.register('sales', SalesViewSet, basename='sales')
router_v1.register('shops', ShopsViewSet, basename='shops')
router_v1.register('forecast', ForecastViewSet, basename='forecast')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('forecast/', ForecastDataView.as_view(), name='forecast-data'),
    # path('forecast', views.create_forecast),
    # path('forecast', views.get_forecast),
]