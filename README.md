Formulari php que crea un esdeveniment de google calendar a partir de la ultima query SQL

De moment et crea el esdeveniment al calendari general de l'usuari que inicia sessió al pas 3

Posar en marxa:
  El codi esta preparat per a funcionar directament, nomes s'ha de cambiar les dades de la BBDD a .py i .php
  Una vegada el codi s'hagi importat, i les credencials descarregades, s'ha d'executar .py per a inicar sessió a Google Calendar

DEPENDENCES
- PIP: google-api-python-client
- PIP: google-auth-oauthlib
- PIP: mysql-connector-python
 
API
  1. Registra una nova api calendar a https://console.cloud.google.com/
     - "Selecciona un proyecto"
     - "Proyecto nuevo" --> emplenar info
     - "APIs i servicios"
     - Buscar "Google Calendar API"
     - "Habilitar"
       
  2. Crea credencials OAuth
     - "Credenciales"
     - "Crear Credenciales" --> "Cuenta de Servicio"
       - Emplenar:
           - "Nombre"
           - "Id"
       - "Continuar"
       - Deixar rol en blanc
       - "Continuar"
       - "Listo"
      
     - "Claves" --> "Agregar clave" --> "JSON"
     - "Crear"
     - Moure JSON a l'arrel, i configurar al codi
