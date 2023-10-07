from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesAPIView,
    ForecastCreateAPIView,
    ForecastViewSet,
    SalesViewSet,
    ShopsAPIView,
    UsersViewSet
)
from users.views import CustomAuthToken

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet)


urlpatterns = [
    path('', include(router_v1.urls)),
    path('forecast/', ForecastViewSet.as_view({'get': 'list'}), name='forecast'),
    path('forecast/create/', ForecastCreateAPIView.as_view(), name='forecast-create'),
    path('categories/', CategoriesAPIView.as_view(), name='categories'),
    path('sales/', SalesViewSet.as_view(), name='sales'),
    path('shops/', ShopsAPIView.as_view(), name='shops'),
    path('auth/', CustomAuthToken.as_view(), name='auth')
]
