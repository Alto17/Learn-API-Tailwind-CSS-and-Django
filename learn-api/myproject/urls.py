from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',include('weather.urls')),
    path('cat/',include('cat.urls')),
    path('anime/',include('anime.urls'))
]
