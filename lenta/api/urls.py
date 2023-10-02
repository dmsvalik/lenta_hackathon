from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesAPIView,
    ForecastDataView,
    SalesAPIView,
    ShopsAPIView,
    UsersViewSet
)
from users.views import CustomAuthToken

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UsersViewSet, basename='users')
# router_v1.register('forecast', ForecastViewSet, basename='forecast')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('forecast/', ForecastDataView.as_view(), name='forecast-data'),
    path('shops/', ShopsAPIView.as_view()),
    path('sales/', SalesAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view()),
    path('auth/', CustomAuthToken.as_view(), name='auth')
    # path('forecast', views.create_forecast),
    # path('forecast', views.get_forecast),
]
