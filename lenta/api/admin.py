from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.views import LoginView
from categories.models import Categories
from forecast.models import Forecast, ForecastSales, SalesUnits
# from .forms import CustomAuthenticationForm
from .models import CustomUser
from sales.models import FactSales, Sales
from shops.models import Shops


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories)


class ForecastAdmin(admin.ModelAdmin):
    pass

admin.site.register(Forecast)
admin.site.register(ForecastSales)
admin.site.register(SalesUnits)


class SalesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sales)


class FactSalesAdmin(admin.ModelAdmin):
    pass

admin.site.register(FactSales)


class ShopsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shops)