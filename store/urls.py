from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.catalog,name="catalog"),
    path('cart/',views.cart,name="cart"),
    path('cart/remove/',views.removeFromCart,name="remove"),
    path('cart/checkout/',views.checkout,name="checkout"),
    path('cart/checkout/complete/',views.completeOrder,name="completeOrder"),
    path('admin-login/', views.adminLogin, name='admin_login'),
    path('admin-panel/', views.adminDashboard, name='admin'),
]
