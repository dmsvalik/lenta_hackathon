from django.contrib import admin
from categories.models import Categories
from forecast.models import Forecast, SalesUnits
from sales.models import Sales
from shops.models import Shops


class CategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories)


class ForecastAdmin(admin.ModelAdmin):
    pass

admin.site.register(Forecast)


class SalesUnitsAdmin(admin.ModelAdmin):
    pass

admin.site.register(SalesUnits)


class SalesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sales)


class ShopsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shops)