from django.shortcuts import render
from .utils import *


# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            "informacion": {
                "tarjeta": {
                    "tipo": "Bip!",
                    "saldo": "3.000",
                    "numero": "123456789",
                },
                "lineas": getMetroLines(),
                "micros": getMicros(),
            }
        }
    )
