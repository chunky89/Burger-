from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
   path('pizza', views.pizza, name='pizza'),
   path('burger', views.burger, name="burgers"),
   path('order', views.order, name="order"),
]