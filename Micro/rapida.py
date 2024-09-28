import os, time
import argparse
import requests # pip install request
from bs4 import BeautifulSoup # pip install BeautifulSoup4
os.system("clear")

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--paradero', default='PD198', required=True)
parser.add_argument('-m', '--micro', default='210')
args = parser.parse_args()

API = "http://web.smsbus.cl/web/buscarAction.do"

PARADERO = args.paradero
MICRO = args.micro

# CREAR SESION
sesion = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Content-Type": "application/x-www-form-urlencoded",
}
peticion = sesion.get(API+"?d=cargarServicios")
html = peticion.text

# GENERA LA PETICION PARA VER LAS MICROS CERCANAS
peticion = sesion.get(API+f"?d=busquedaRapida&busqueda_rapida={PARADERO}+{MICRO}", headers=headers)
html = peticion.text

# COCINA LA SOPA
soup = BeautifulSoup(html, "html.parser")
# OBTIENE LOS DATOS IMPORTANTES
paradero = soup.find("div", {"id": "nombre_paradero_respuesta"}).get_text()
micros = soup.find_all("div", {"id": "proximo_respuesta"})
print(f"{MICRO} @ {PARADERO}", paradero)
# POR CADA MICRO DISPONIBLE
for micro in micros:
    patente = str(micro.contents[1].get_text()).strip()
    tiempo = str(micro.contents[3].get_text()).strip()
    distancia = str(micro.contents[5].get_text()).strip()
    print()
    print("Patente:", patente)
    print("Tiempo:", tiempo)
    print("Distancia:", distancia)
    print()
    time.sleep(.5)
