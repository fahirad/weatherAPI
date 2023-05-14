from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather_api_app.models import Weather
from rest_framework.views import APIView
# create and return data

# To be called when hitting a current weather endpoint
class CurrentWeather(APIView):
    def post(self, request):
        
        city = request.data.get('city')

        if not city:
            return Response({'error': 'Please provide a city name'}, status=400)

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c61631d8485047e7d9ecc565cfac1c42'        
        response = requests.get(url.format(city))
        # city_weather = requests.get(url)

        if response.status_code != 200:
            return Response({'error': 'Invalid city name or API key'}, status=400)
        city_weather = response.json()
        weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'], 
                'description' : city_weather['weather'][0]['description'],
        }

        return Response(weather)

# To be called when hitting a forecast weather endpoint
class ForecastWeather(APIView):
    def post(self, request):
        
        city = request.data.get('city')

        if not city:
            return Response({'error': 'Please provide a city name'}, status=400)

        url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&cnt=10&mode=json&appid=c61631d8485047e7d9ecc565cfac1c42&units=metric'        
        response = requests.get(url.format(city))
        # city_weather = requests.get(url)

        if response.status_code != 200:
            return Response({'error': 'Invalid city name or API key'}, status=400)
        city_weather = response.json()
        
        # todo: handle averagin temps
        days = []
        for i in city_weather['list']:
            day = i['dt_txt'][:10]
            if day not in days:
                days.append(day)
                average_temp = i['main']['temp']
            else:
                average_temp += i['main']['temp']
            

        # weather = {
        #         'city' : city,
        #         'temperature' : round((city_weather['main']['temp']-32)/1.8), # converting fahrenheit to celsius
        #         'description' : city_weather['weather'][0]['description'],
        # }

        return Response(city_weather)
    
# To be called when hitting a historical weather endpoint
# Uses Statistical API from OpenWeatherMap for a monthly statistical data
class HistoryWeather(APIView):
    def post(self, request):
        
        city = request.data.get('city')

        if not city:
            return Response({'error': 'Please provide a city name'}, status=400)

        url = 'https://history.openweathermap.org/data/2.5/aggregated/year?q={}&appid=c61631d8485047e7d9ecc565cfac1c42&units=metric'   #paid?    
        response = requests.get(url.format(city)) # The input should be a city,country_code e.g. London,UK
        # city_weather = requests.get(url)

        if response.status_code != 200:
            return Response({'error': 'Invalid city name or API key'}, status=400)
        city_weather = response.json()

        return Response(city_weather)


