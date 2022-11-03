from django.urls import path
from . import views

urlpatterns = [
    path('logad',views.log),
    path('adhome',views.addetails),
    path('userd',views.userde),
    path('stocks',views.stock),
    path('orders',views.order),
]
   