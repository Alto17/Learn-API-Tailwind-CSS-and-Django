from django.shortcuts import render,HttpResponse

import os
from dotenv import load_dotenv
import requests
import random

load_dotenv()
api_key = os.getenv('API_KEY_ANIME')

# Create your views here.
def index(request):
    anime_list = []
    
    if request.method == 'GET' and request.GET.get('get_anime'):
        url = 'https://api.jikan.moe/v4/top/anime'
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            animes = random.sample(data["data"], 3)
            
            for anime in animes:
                titleAnime = anime['title']
                imageAnime = anime['images']['jpg']['image_url']
                anime_list.append({'title': titleAnime, 'image_url': imageAnime})
        else:
            return HttpResponse(response.status_code)
    
    
    context = {
        'title':'Rekomendasi Anime',
        'heading':'Anime',
        'sub_heading':'rekomendasi anime :',
        'page':'anime',
        'anime_list': anime_list,
    }
    return render(request,'index.html',context)