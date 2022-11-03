
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('shop',views.shop),
    path('sigp',views.signup),
    path('log',views.login),
    path('toy',views.toys),
    path('fashion',views.fashions),
    path('food',views.foods),
    path('special',views.specials),
    path('buy',views.buyones),
    path('cart',views.carts),
    


]