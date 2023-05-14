from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from weather_api_app.models import Weather
from rest_framework.views import APIView
# create and return data

# Create your views here.
# @api_view(['POST', 'GET'])
# def city_weather(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c61631d8485047e7d9ecc565cfac1c42'
#     if request.method == 'POST':
#         city = request.POST['city']
#         city_weather = requests.get(url.format(city)).json()
#         # if city_weather.status_code == 200:
#         weather = {
#                 'city' : city,
#                 'temperature' : city_weather['main']['temp'],
#                 'description' : city_weather['weather'][0]['description'],
#                 'icon' : city_weather['weather'][0]['icon']
#             }

#         return Response(weather)
    
    # else:
    #     return JsonResponse({'error': 'Invalid city name'}, status=400)
    
class CityWeather(APIView):
    def post(self, request):
        
        city = request.data.get('city')

        if not city:
            return Response({'error': 'Please provide a city name'}, status=400)

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c61631d8485047e7d9ecc565cfac1c42'        
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



