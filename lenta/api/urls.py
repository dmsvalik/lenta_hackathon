from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
<<<<<<< HEAD
    CategoriesAPIView,
    ForecastDataView,
    SalesAPIView,
    ShopsAPIView,
    UsersViewSet
=======
    CategoriesViewSet,
    ForecastCreateAPIView,
    ForecastViewSet,
    SalesViewSet,
    ShopsViewSet
>>>>>>> forcast_fix
)
from users.views import CustomAuthToken

app_name = 'api'

router_v1 = DefaultRouter()
<<<<<<< HEAD
router_v1.register('users', UsersViewSet, basename='users')
# router_v1.register('forecast', ForecastViewSet, basename='forecast')
=======
>>>>>>> forcast_fix


urlpatterns = [
    path('', include(router_v1.urls)),
<<<<<<< HEAD
    path('forecast/', ForecastDataView.as_view(), name='forecast-data'),
    path('shops/', ShopsAPIView.as_view()),
    path('sales/', SalesAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view()),
    path('auth/', CustomAuthToken.as_view(), name='auth')
    # path('forecast', views.create_forecast),
    # path('forecast', views.get_forecast),
=======
    path('forecast/', ForecastViewSet.as_view({'get': 'list'}), name='forecast'),
    path('forecast/create/', ForecastCreateAPIView.as_view(), name='forecast-create'),
    path('categories/', CategoriesViewSet.as_view({'get': 'list'}), name='categories'),
    path('sales/', SalesViewSet.as_view({'get': 'list'}), name='sales'),
    path('shops/', ShopsViewSet.as_view({'get': 'list'}), name='shops'),
>>>>>>> forcast_fix
]
