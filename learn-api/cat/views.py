from django.shortcuts import render,HttpResponse

import os

import requests


# Create your views here.
def get_cat(request):
    cat_image = None
    
    if request.method == 'GET' and request.GET.get('get_image'):
        url = "https://api.thecatapi.com/v1/images/search"
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            cat_image = data[0]["url"]
        else:
            return HttpResponse("Gagal mengambil data:", response.status_code)
                
    
    context= {
        'title':'Cat 😻',
        'heading':'Looking for Cat Pictures',
        'sub_heading':'Find Your Cat',
        'cat_image': cat_image,
        'page':'cat'
    }
    return render(request,'index.html',context)