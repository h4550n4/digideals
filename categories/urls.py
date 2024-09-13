from django.urls import path
from . import views

urlpatterns= [
    path('', views.category_list, name='category_list'),
    path('<int:category_id>', views.category_products, name='category_products'),
]