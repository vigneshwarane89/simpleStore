from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.catalog,name="catalog"),
    path('cart/',views.cart,name="cart"),
    path('cart/remove/',views.removeFromCart,name="remove")
]
