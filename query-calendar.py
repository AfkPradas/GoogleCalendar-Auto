import mysql.connector
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
import os.path
import sys

DB_CONFIG = {
    'host': 'localhost',
    'user': '',
    'password': '',
    'database': ''
}

DB_CONFIG_DNI = {
    'host': 'localhost',
    'user': '',
    'password': '',
    'database': ''
}

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = '.json'

def authenticate_google():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def get_res(id):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM reserva WHERE id=%s;"
    cursor.execute(query, (id,))
    event = cursor.fetchone()

    query = "SELECT sala FROM sala WHERE id=%s;"
    cursor.execute(query, (str(event["sala"]),))
    sala = cursor.fetchone()

    cursor.close()
    connection.close()
    
    return event, sala

def get_name_dni(dni):
    connection = mysql.connector.connect(**DB_CONFIG_DNI)
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT nom FROM dni WHERE dni=%s;"
    cursor.execute(query, (dni,))
    event = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return event

def create_google_event(event, name, sala):
    creds = authenticate_google()
    service = build('calendar', 'v3', credentials=creds)

    calendarId = ""

    assist = event["num_assistents"] if event["num_assistents"] != "NULL" else "No definit"

    inici_iso = datetime.strptime(event['hora_inici'], "%d/%m/%Y %H:%M").isoformat()
    fi_iso = datetime.strptime(event['hora_fi'], "%d/%m/%Y %H:%M").isoformat()

    event_data = {
        'summary': name['nom'],
        'location': sala['sala'],
        'description': str(event["descripcio"]) + "\n\n \n\n" + "Assistents: " + str(assist),
        'start': {'dateTime': inici_iso, 'timeZone': 'Europe/Madrid'},
        'end': {'dateTime': fi_iso, 'timeZone': 'Europe/Madrid'},
    }

    created_event = service.events().insert(calendarId=calendarId, body=event_data).execute()

    return created_event

def main():
    if len(sys.argv) < 2:
        print("No variable")
        sys.exit(1)
    id = sys.argv[1]
    last_event, sala = get_res(id)
    dni_name = get_name_dni(last_event['userdni'])
    
    if last_event:
        create_google_event(last_event, dni_name, sala)

if __name__ == '__main__':
    main()
