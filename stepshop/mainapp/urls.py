
from django.urls import path

from mainapp.views import index, about, products

urlpatterns = [
    path('', index),
    path('about/', about),
    path('products/', products),
]
