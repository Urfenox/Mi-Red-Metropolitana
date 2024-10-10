# Mi Red Metropolitana
Se trata de una pequeña aplicación web que permite ver información útil sobre tu tarjeta Bip!, estado del metro y micros cercanas a un paradero favorito.  
> Proyecto personal pensado para espejo inteligente *idk*.  

Características:  

 - Muestra información sobre tu Tarjeta Bip!.  
 - Muestra información sobre el estado de la red de Metro de Santiago.  
 - Muestra las micros seleccionadas cercanas a un paradero definido.  

## Tecnologías usadas

 1. [Django](https://www.djangoproject.com/): El framework web para Python.  
 2. [Bootstrap](https://getbootstrap.com/): El framework CSS para estilizado.  
 3. [htmx](https://htmx.org/): Un framework para sitios web dinámicos (sin JavaScript 😊)  
 4. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): Una librería Python para [web scraping](https://es.wikipedia.org/wiki/Web_scraping#T%C3%A9cnicas).  

## Setup
Debes configurar tu tarjeta, el paradero y las micros de este.  

 1. Dentro de la carpeta `aplicacion` deberás crear un archivo llamado `secretos.py`.  
 2. En el archivo `aplicacion/secretos.py` pega el siguiente fragmento de código:  
 ```python
 # SI ES TNE (Pase escolar): SE DEBE INDICAR EL RUT DEL TITULAR
 TARJETA = str(f"1234567890")
 RUT = str(f"12345678{"-9"}")
 # SI ES BIP!: SOLO SE INGRESA EL NUMERO DE LA TARJETA, AL RUT SE LE DEJA UN "0"
 # TARJETA = str(f"1234567890")
 # RUT = str(f"0")

 PARADERO = "PG138" # CODIGO DEL PARADERO "Parada 4 / Paradero 31 Santa Rosa"
 MICROS = ["212", "233"] # SERVICIOS (micros) DEL PARADERO
 ```
 3. Guarda el archivo y ya estás listo.  

### Puesta en marcha
Usa Django (con planes de pasarlo a Flask).  

 1. Abre una consola del sistema dentro de la carpeta del proyecto.  
 2. Crea un entorno virtual de Python  
    `py -m venv .venv`  
 3. Entra al entorno virtual  
    `source .venv/bin/activate`  
 5. Instala los paquetes necesarios a través de `pip` con `requirements.txt`  
    `pip install -r requirements.txt`  
 7. Inicia el servidor Django  
    `py manage.py runserver`  

Una vez realizados los pasos, podrás ver el sitio dirigiéndote a http://localhost:8000/.  

# TODO

 - Aceptar Bip!QR
 - Notificacion mediante Pushover sobre saldo bajo.
 - Permitir varios paraderos ?

> Para mí el proyecto está listo, está en la cúspide de perfección. No hay nada que pueda mejorarlo, menos un ser mortal.  

![Works on my Machine](https://dev.crizacio.com/ZZaci0/assets/images/works-on-my-machine.png)
