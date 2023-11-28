
from django.urls import path
from .views import basket, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path('', basket, name="index"),
    path('add/<int:pk>/', basket_add, name="add"),
    path('remove/<int:pk>/', basket_remove, name="remove"),
]
