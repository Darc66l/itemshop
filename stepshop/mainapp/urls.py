
from django.urls import path

from mainapp.views import index, about, products, contact, singleproduct

urlpatterns = [
    path('', index),
    path('about/', about),
    path('products/', products),
    path('contact/', contact),
    path('SP/', singleproduct)
]
