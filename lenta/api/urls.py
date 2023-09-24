from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import *

app_name = 'api'

router_v1 = DefaultRouter()
# router_v1.register('trades', TradesViewSet, basename='trades') # Можно менять это на будущее


urlpatterns = [
    path('', include(router_v1.urls)),
]