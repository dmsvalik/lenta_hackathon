from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesAPIView,
    ForecastViewSet,
    SalesViewSet,
    ShopsViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('forecast', ForecastViewSet, basename='forecast')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('shops/', ShopsViewSet.as_view(), name='shops'),
    path('sales/', SalesViewSet.as_view(), name='shops')
]
