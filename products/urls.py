from django.urls import path
from . import views

urlpatterns = [
    path('productlist', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('', views.home_view, name='home')
]