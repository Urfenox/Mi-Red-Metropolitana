# Mi Red Metropolitana
Proyecto personal pensado para espejo inteligente idk.  

Características:  

 - Muestra información sobre tu Tarjeta Bip!.  
 - Muestra información sobre el estado de la red de Metro de Santiago.  
 - Muestra las micros seleccionadas cercanas a un paradero definido.  

## Setup
Debes configurar tu tarjeta, el paradero y las micros de este.  

 1. Dentro de `aplicacion` deberás crear un archivo llamado `secretos.py`.  
 2. Dentro de `aplicacion/secretos.py` pega el siguiente fragmento de código:  
 ```python
 # SI ES TNE (Pase escolar): SE DEBE INDICAR EL RUT DEL TITULAR
 TARJETA = str(f"1234567890")
 RUT = str(f"12345678{"-9"}")
 # SI ES BIP!: SOLO SE INGRESA EL NUMERO DE LA TARJETA, EL RUT SE LE DEJA UN "0"
 # TARJETA = str(f"1234567890")
 # RUT = str(f"0")

 PARADERO = "PG138" # CODIGO DEL PARADERO "Parada 4 / Paradero 31 Santa Rosa"
 MICROS = ["212", "233"] # SERVICIOS (micros) DEL PARADERO
 ```
 3. Guarda el archivo y ya estás listo.  

### Puesta en marcha
Usa Django (con planes de pasarlo a Flask).  

 1. Crea un entorno virtual de Python `py -m venv .venv`.  
 2. Entra al entorno virtual source `source .venv/bin/activate`.  
 3. Instala los paquetes necesarios a través de `pip` con `requirements.txt` `pip install -r requirements.txt`.  
 4. Inicia el servidor Django `py manage.py runserver`.  
