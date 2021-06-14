from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     # all
     path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),
     path('', views.homepage, name='home'),
     # employee
     path('employee/', views.admin, name='employee'),
     path('employee/product', views.product, name='product'),
     path('employee/product/add', views.add_product, name='add_product'),

     #customer
     path('homepage/', views.customer, name='customer'),
]
