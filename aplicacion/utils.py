from .secretos import *
from .servicios import *

tarjeta = Tarjeta(TARJETA, RUT)
metro = Metro()
micro = Transantiago(PARADERO, MICROS)

def getTarjeta():
    bip = tarjeta.obtenerInformacion()
    return bip

def getMetro():
    lineas = metro.obtenerEstados()
    return lineas

def getMicros():
    micros = micro.obtenerMicros()
    return micros
