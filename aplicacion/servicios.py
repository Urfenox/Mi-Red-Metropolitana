import json
import requests # pip install request
from bs4 import BeautifulSoup # pip install BeautifulSoup4


class Tarjeta():

    API = "http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/SesionPortalServlet"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0',
        "Content-Type": "application/x-www-form-urlencoded",
    }
    session = requests.Session()
    sessionInfo = None

    def __init__(self, tarjeta, rut):
        self.tarjeta = tarjeta
        self.rut = rut
        PAYLOAD_SESION = {
            "accion": "6",
            "NumDistribuidor": "99",
            "NomUsuario": "usuInternet",
            "NomHost": "AFT",
            "NomDominio": "aft.cl",
            "Trx": "",
            "RutUsuario": self.rut,
            "NumTarjeta": self.tarjeta,
            "bloqueable": "0"
        }
        # INICIA SESION
        peticion = self.session.post(self.API, headers=self.headers, data=PAYLOAD_SESION)
        html = peticion.text

        soup = BeautifulSoup(html, "html.parser")
        myFORM = soup.find("form", {"id": "formMenuPrincipal"})
        self.sessionInfo = myFORM
    
    tarjeta = ""
    rut = "0"

    def obtenerInformacion(self):
        # REALIZA LA SOLICITUD DE SALDO
        PAYLOAD_SALDO = {
            "KSI": self.sessionInfo.contents[1].get('value'),
            "accion": "6",
            "itemms": "1000",
            "item": "1",
            "fechalogeo": self.sessionInfo.contents[9].get('value'),
            "DiasMov": "90",
            "FechaInicioMovimientos": ""
        }
        peticion = self.session.post(self.API, headers=self.headers, data=PAYLOAD_SALDO)
        html = peticion.text

        # TOMA LOS DATOS
        soup = BeautifulSoup(html, "html.parser")
        datos = soup.find_all("td", {"class": "verdanabold-ckc"})
        tipo = soup.find_all("span", {"class": "arial12-bold-azul"})

        saldo = str(datos[5].get_text()).replace("$", "").strip()
        fecha = str(datos[7].get_text()).strip()

        return {
            "tipo": "Bip!" if len(tipo) < 2 else "TNE",
            "saldo": saldo,
            "fecha": fecha,
            "numero": self.tarjeta,
        }


class Metro():

    API = "https://www.metro.cl/api/estadoRedDetalle.php"

    def __init__(self):
        pass

    def obtenerEstados(self):
        peticion = requests.get(self.API)
        lineas = json.loads(peticion.text)

        retorno = []
        for linea in lineas:
            nombre = str(linea).upper()
            linea = lineas[linea]
            estado = linea["estado"]
            color = "#39974b" if estado == '1' else "#717100"
            mensaje = str(linea["mensaje_app"])
            retorno.append({
                "nombre": nombre,
                "color": color,
                "mensaje": mensaje,
            })
        return retorno


class Transantiago():

    API = "http://web.smsbus.cl/web/buscarAction.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    sesion = requests.Session()

    def __init__(self, paradero, micros):
        self.paradero = paradero
        self.micros = micros
        # CREAR SESION
        peticion = self.sesion.get(self.API+"?d=cargarServicios")
        html = peticion.text
    
    paradero = ""
    micros = "0"

    def obtenerMicros(self):
        # GENERA LA PETICION PARA VER LAS MICROS CERCANAS
        peticion = self.sesion.get(self.API+f"?d=busquedaParadero&ingresar_paradero={self.paradero}", headers=self.headers)
        html = peticion.text

        # COCINA LA SOPA
        soup = BeautifulSoup(html, "html.parser")
        # OBTIENE LOS DATOS IMPORTANTES
        paradero = str(soup.find("div", {"id": "nombre_paradero_respuesta"}).get_text()).strip().replace("Paradero: ", "")
        cercanas = soup.find_all("div", {"id": "siguiente_respuesta"})
        lejanas = soup.find_all("div", {"id": "proximo_solo_paradero"})

        micros = [] # todas las micros, ordenadas de menor a mayor distancia
        micros.extend(cercanas)
        micros.extend(lejanas)
        # elimina las micros que no nos importan
        micros = list(filter(lambda x : str(x.contents[1].get_text()).strip() in self.micros, micros))
        # ordena de menor a mayor distancia
        micros.sort(key=lambda x: int(str(x.contents[7].get_text()).strip().replace(" mts.", "")))

        retorno = []
        for micro in micros:
            servicio = str(micro.contents[1].get_text()).strip()
            patente = str(micro.contents[3].get_text()).strip()
            tiempo = str(micro.contents[5].get_text()).strip()
            distancia = str(micro.contents[7].get_text()).strip().replace(" mts.", "")
            if "Llegando." in tiempo: tiempo += ".."
            retorno.append({
                "servicio": servicio,
                "patente": patente,
                "llegada": tiempo,
                "distancia": distancia,
            })

        return {
            "paradero": self.paradero + " " + paradero,
            "micros": retorno[:3],
        }
