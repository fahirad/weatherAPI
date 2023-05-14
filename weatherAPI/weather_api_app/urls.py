
from django.contrib import admin
from django.urls import path, include
from weather_api_app.views import CityWeather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current/', CityWeather.as_view())
]
