from django.urls import path
from . import views

urlpatterns= [
    path('categories', views.category_list, name='category_list'),
    path('categories/<int:category_id>', views.category_products, name='category_products'),
]