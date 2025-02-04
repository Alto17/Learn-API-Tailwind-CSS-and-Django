from django.urls import path

from . import views

urlpatterns = [
    path('',views.get_cat,name='get_cat')
]
