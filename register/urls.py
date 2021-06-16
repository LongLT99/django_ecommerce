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
     path('addtocart/<int:id>', views.addtocart, name="addtocart"),
     path('cart/', views.cart, name="cart"),
     path('confirm/', views.confirm, name="confirm"),
     path('order/', views.order, name="order"),
     path('orderdetail/<int:id>', views.orderdetail, name="orderdetail"),
]
