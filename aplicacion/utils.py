from .secretos import *
from .servicios import *

def getTarjeta():
    tarjeta = Tarjeta(TARJETA, RUT)
    bip = tarjeta.obtenerInformacion()
    return bip

def getMetro():
    metro = Metro()
    lineas = metro.obtenerEstados()
    return lineas

def getMicros():
    micro = Transantiago(PARADERO, MICROS)
    micros = micro.obtenerMicros()
    return micros
