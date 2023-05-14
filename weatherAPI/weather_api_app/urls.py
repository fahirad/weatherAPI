
from django.contrib import admin
from django.urls import path, include
from weather_api_app.views import CurrentWeather, ForecastWeather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('current/', CurrentWeather.as_view()),
    path('forecast/', ForecastWeather.as_view())

]
