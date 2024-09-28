from django.urls import path
from .views import *

app_name = "aplicacion"

urlpatterns = [
    path('', index, name="index"),
]
