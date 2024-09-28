from django.shortcuts import render
from .utils import *


# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            "informacion": {
                "tarjeta": getTarjeta(),
                "lineas": getMetro(),
                "micros": getMicros(),
            }
        }
    )
