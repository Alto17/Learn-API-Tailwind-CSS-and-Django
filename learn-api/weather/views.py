from django.shortcuts import render,HttpResponse


import os
from dotenv import load_dotenv
import requests


load_dotenv()
api_key = os.getenv('API_KEY_WEATHER')

def get_weather(request):
    weather_data = None
    latitude = None
    longitude = None
    city_name = None
    weather = None
    tempe = None
    
    if request.method == "POST":
        location = request.POST.get('location')
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(url,params=params)
        if response.status_code == 200:
            weather_data = response.json()
            latitude = weather_data['coord']['lat']
            longitude = weather_data['coord']['lon']
            city_name = weather_data['name']
            weather = weather_data['weather'][0]['description']
            tempe = weather_data['main']['temp']
        else:
            return HttpResponse(f'Error {response.status_code}\n{response.text}')
        
        
    context = {
        'title':'Cek your weather',
        'heading': 'Weather Information',
        'sub_heading':'Enter a location',
        'weather_data': weather_data,
        'city_names': city_name,
        'weather': weather,
        'tempe': tempe,
        'long': longitude,
        'lat':latitude,
        'page':'weather'
    }
    
    return render(request,'index.html',context)
