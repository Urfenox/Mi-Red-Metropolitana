import os, time
import argparse
import requests # pip install request
from bs4 import BeautifulSoup # pip install BeautifulSoup4
os.system("clear")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--tarjeta', default='12345678', required=True)
parser.add_argument('-r', '--rut', default='0')
parser.add_argument('-m', '--movimientos', default=3, type=int)
args = parser.parse_args()

URL = "http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/SesionPortalServlet"

RUT = args.rut # si es Bip! va un 0, si es TNE se pone el rut del titular
TARJETA = args.tarjeta
NMOVIMIENTOS = args.movimientos

PAYLOAD1 = {
	"accion": "6",
	"NumDistribuidor": "99",
	"NomUsuario": "usuInternet",
	"NomHost": "AFT",
	"NomDominio": "aft.cl",
	"Trx": "",
	"RutUsuario": RUT,
	"NumTarjeta": TARJETA,
	"bloqueable": "0"
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
    "Content-Type": "application/x-www-form-urlencoded",
}
# INICIA SESION
session = requests.Session()
peticion = session.post(URL, headers=headers, data=PAYLOAD1)
html = peticion.text

soup = BeautifulSoup(html, "html.parser")
myFORM = soup.find("form", {"id": "formMenuPrincipal"})

# REALIZA LA SOLICITUD DE SALDO
PAYLOAD2 = {
	"KSI": myFORM.contents[1].get('value'),
	"accion": "6",
	"itemms": "1000",
	"item": "1",
	"fechalogeo": myFORM.contents[9].get('value'),
	"DiasMov": "90",
	"FechaInicioMovimientos": ""
}
peticion = session.post(URL, headers=headers, data=PAYLOAD2)
html = peticion.text

# TOMA LOS DATOS
soup = BeautifulSoup(html, "html.parser")
# busca toda etiqueta <td> con la clase "verdanabold-ckc"
myTDs = soup.find_all("td", {"class": "verdanabold-ckc"}) # es un array

# IMPRIME SALDO Y FECHA
print()
print(myTDs[5].get_text()) # llamamos el metodo para obtener el texto
print(myTDs[7].get_text())
print()

# REALIZA LA SOLICITUD DE MOVIMIENTOS
PAYLOAD3 = {
	"KSI": myFORM.contents[1].get('value'),
	"accion": "1",
	"itemms": "3000",
	"item": "2",
	"fechalogeo": myFORM.contents[9].get('value'),
	"DiasMov": "90",
	"FechaInicioMovimientos": ""
}
peticion = session.post("http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/ComercialesPortalServlet", headers=headers, data=PAYLOAD3)
html = peticion.text

# TOMA LOS DATOS
soup = BeautifulSoup(html, "html.parser")
myTRs = soup.find_all("tr", {"class": "arial12-azul"})[:NMOVIMIENTOS]

for item in myTRs:
    numero = str(item.contents[3].get_text()).strip()
    tipo = str(item.contents[5].get_text()).strip()
    fechahora = str(item.contents[7].get_text()).strip()
    lugar = str(item.contents[9].get_text()).strip()
    monto = str(item.contents[11].get_text()).strip()
    saldo = str(item.contents[13].get_text()).strip()
    print()
    print("N° Transaccion:", numero)
    print("Tipo:", tipo)
    print("Fecha y hora:", fechahora)
    print("Lugar:", lugar)
    print("Monto:", "-$" + monto if tipo == "Uso Tarjeta" else monto)
    print("Saldo:", "$" + saldo if tipo == "Uso Tarjeta" else saldo)
    print()
    time.sleep(.5)
