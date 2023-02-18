from django.shortcuts import render
from django.http import HttpResponse
from. models import Pizza, Burger
# Create your views here.

def index(request):
    ctx = {'active_link': 'index'}
    return render(request, 'menu/index.html')

def pizza(request):
    pizzas = Pizza.objects.all()
    ctx = {'pizza': pizzas, 'active_link': 'pizza'}
    return render(request, 'menu/pizza.html', ctx)

def burger(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers, 'active_link': 'burger'}
    return render(request, 'menu/burgers.html', ctx)

def order(request):
    ctx = {'active_link': 'order'}
    return render(request, 'menu/order.html', ctx)