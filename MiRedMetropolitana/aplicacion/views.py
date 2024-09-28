from django.shortcuts import render
from .utils import *


# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            "informacion": {
                "tipo": "Bip!",
                "saldo": "3.000",
                "tarjeta": "123456789",
                "lineas": getMetroLines(),
                "micros": getMicros(),
            }
        }
    )
