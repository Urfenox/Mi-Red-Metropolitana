from django.shortcuts import render
from .utils import *


# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            "tarjeta": getTarjeta(),
            "lineas": getMetro(),
            "micros": getMicros(),
        }
    )

def bip(request):
    return render(
        request,
        "servicios/bip.html",
        {
            "tarjeta": getTarjeta()
        }
    )

def metro(request):
    return render(
        request,
        "servicios/metro.html",
        {
            "lineas": getMetro(),
        }
    )

def micro(request):
    return render(
        request,
        "servicios/micro.html",
        {
            "micros": getMicros(),
        }
    )
