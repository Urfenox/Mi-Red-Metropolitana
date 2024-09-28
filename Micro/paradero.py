import os, time
import requests # pip install request
from bs4 import BeautifulSoup # pip install BeautifulSoup4
os.system("clear")

API = "http://web.smsbus.cl/web/buscarAction.do"

PARADERO = "PG138"
MICROS = ["212", "233"]

# CREAR SESION
sesion = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Content-Type": "application/x-www-form-urlencoded",
}
peticion = sesion.get(API+"?d=cargarServicios")
html = peticion.text

# GENERA LA PETICION PARA VER LAS MICROS CERCANAS
peticion = sesion.get(API+f"?d=busquedaParadero&ingresar_paradero={PARADERO}", headers=headers)
html = peticion.text

# COCINA LA SOPA
soup = BeautifulSoup(html, "html.parser")
# OBTIENE LOS DATOS IMPORTANTES
cercanas = soup.find_all("div", {"id": "siguiente_respuesta"})
lejanas = soup.find_all("div", {"id": "proximo_solo_paradero"})
# POR CADA MICRO DISPONIBLE
#ordenar por distancia uwu
micros = [] # todas las micros, ordenadas de menor a mayor distancia
for micro in cercanas:
    servicio = str(micro.contents[1].get_text()).strip()
    patente = str(micro.contents[3].get_text()).strip()
    tiempo = str(micro.contents[5].get_text()).strip()
    distancia = str(micro.contents[7].get_text()).strip().replace(" mts.", "")
    if servicio in MICROS:
        print()
        print("Servicio:", servicio)
        print("Patente:", patente)
        print("Tiempo:", tiempo)
        print("Distancia:", distancia, "mts.")
        micros.append(micro)
        time.sleep(.5)

print("---")

# TODO : 
#   - se debe tener al menos 3 micros dentro del array micros.
#   - las cercanas primero, luego la mas cercana dentro de lejanas.

# menordistancia = lejanas[0]
# for micro in lejanas:
#     servicio = str(micro.contents[1].get_text()).strip()
#     patente = str(micro.contents[3].get_text()).strip()
#     tiempo = str(micro.contents[5].get_text()).strip()
#     distancia = str(micro.contents[7].get_text()).strip().replace(" mts.", "")
#     if servicio in MICROS:
#         print()
#         print("Servicio:", servicio)
#         print("Patente:", patente)
#         print("Tiempo:", tiempo)
#         print("Distancia:", distancia, "mts.")
#         if int(distancia) < int(str(menordistancia.contents[7].get_text()).strip().replace(" mts.", "")):
#             menordistancia = micro
#             micros.append(micro)
#         time.sleep(.5)

print(micros)
