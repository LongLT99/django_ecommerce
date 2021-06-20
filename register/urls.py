from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # user

    # trang đăng ký
    path('register/', views.register, name='register'),
    # trang đăng nhập
    path('login/', views.login, name='login'),
    # trang chủ
    path('', views.homepage, name='home'),
    # trang chi tiết sản phẩm 
    path('productdetail/<int:id>', views.productdetail, name="productdetail"),

    # employee

    # trang chủ nhân viên
    path('employee/', views.admin, name='employee'),
    # trang quản lý sản phẩm
    path('employee/product', views.product, name='product'),
    # trang thêm sản phẩm
    path('employee/product/add', views.add_product, name='add_product'),
    # trang chỉnh sủa sản phẩm 
    path('employee/editproduct/<int:id>', views.editproduct, name="editproduct"),
    #trang quản lý đơn hàng
    path('employee/order', views.admin_order, name='admin_order'),
    # trang xử lý đơn hàng
    path('employee/orderprocess/<int:id>', views.orderprocess, name="orderprocess"),
    # trang quản lý đánh giá của khách hàng
    path('employee/rating', views.adminrating, name="adminrating"),
    # trang xử lý đánh giá của khách hàng
    path('employee/ratingprocess/<int:id>', views.ratingprocess, name="ratingprocess"),

    # customer

    # trang chủ khách hàng
    path('homepage/', views.customer, name='customer'),
    # thêm hàng và giỏ
    path('addtocart/<int:id>', views.addtocart, name="addtocart"),
    # trang giỏ hàng
    path('cart/', views.cart, name="cart"),
    # trang xác nhận đơn hàng
    path('confirm/', views.confirm, name="confirm"),
    # trang xem đơn hàng
    path('order/', views.order, name="order"),
    # trang chi tiết đơn hàng
    path('orderdetail/<int:id>', views.orderdetail, name="orderdetail"),
    # trang đánh giá sản phẩm
    path('rating/<int:id>', views.rating, name="rating"),

]
