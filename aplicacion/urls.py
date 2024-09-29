from django.urls import path
from .views import *

app_name = "aplicacion"

urlpatterns = [
    path('', index, name="index"),
    path('bip', bip, name="bip"),
    path('metro', metro, name="metro"),
    path('micro', micro, name="micro"),
]
