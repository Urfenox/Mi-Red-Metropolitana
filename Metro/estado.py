import os
import json
import requests
os.system("clear")

API = "https://www.metro.cl/api/estadoRedDetalle.php"

peticion = requests.get(API)
lineas = json.loads(peticion.text)

print(str(lineas["l1"]["mensaje_app"]))

for linea, estado, mensaje, mensaje_app in lineas:
    print(linea)
    print(mensaje_app)
