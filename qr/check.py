import os
import requests
from PIL import Image
from pyzbar.pyzbar import decode
import psycopg2
import json

connection = psycopg2.connect(
    host='127.0.0.1', 
    port= '5432',
    database="qr",
    user="pavelkrolevets",
    password=None,
)
connection.autocommit = True

def create_staging_table(cursor) -> None:
    cursor.execute("""
        DROP TABLE IF EXISTS qr_covid;
        CREATE UNLOGGED TABLE qr_covid (
            vax_num             TEXT,
            vax_id              TEXT,
            fio                 TEXT,
            birthDate           TEXT,
            passport            TEXT,
            qr                  TEXT,
            image_url           TEXT,
            expiredAt           TEXT
        );
    """)

with connection.cursor() as cursor:
     create_staging_table(cursor)


for root, dirs, files in os.walk('./downloads'):
     for file in files:
        try:
            data = decode(Image.open(root+"/"+file))
            if "https://www.gosuslugi.ru/vaccine/cert/verify" in data[0].data.decode('UTF-8'):
                print(root+"/"+file)
                print(data[0].data.decode('UTF-8'))
                id_hash = data[0].data.decode('UTF-8').replace("https://www.gosuslugi.ru/vaccine/cert/verify/", "")
                print(id_hash)
                final_url = "https://www.gosuslugi.ru/api/vaccine/v1/cert/verify/"+id_hash
                r = requests.get(final_url)
                qr = json.loads(r.text)
                print(qr)
                cursor = connection.cursor()
                # create_staging_table(cursor)
                cursor.execute("INSERT INTO qr_covid (vax_num, vax_id,fio,birthDate,passport,qr,image_url,expiredAt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)" , (
                    qr['unrz'],
                    id_hash,
                    qr['fio'],
                    qr['birthdate'],
                    qr['doc'],
                    qr['qr'],
                    root+"/"+file,
                    qr['expiredAt']))
                connection.commit()
            
            
            if "https://www.gosuslugi.ru/covid-cert/verify/" in data[0].data.decode('UTF-8'):
                print(root+"/"+file)
                print(data[0].data.decode('UTF-8'))
                id_hash = data[0].data.decode('UTF-8').replace("https://www.gosuslugi.ru/covid-cert/verify/", "")
                print(id_hash)
                final_url = "https://www.gosuslugi.ru/api/covid-cert/v3/cert/check/"+id_hash
                r = requests.get(final_url)
                qr = json.loads(r.text)
                print(qr)
                cursor = connection.cursor()
                # create_staging_table(cursor)
                cursor.execute("INSERT INTO qr_covid (vax_num,vax_id,fio,birthDate,passport,qr,image_url,expiredAt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)" , (
                    qr['items'][0]['unrzFull'],
                    qr['items'][0]['unrzFull'],
                    qr['items'][0]['attrs'][0]['value'],
                    qr['items'][0]['attrs'][1]['value'],
                    qr['items'][0]['attrs'][2]['value'],
                    qr['items'][0]['qr'],
                    root+"/"+file,
                    qr['items'][0]['expiredAt']))
                connection.commit()
        except Exception:
            print("QR decode error")

connection.close()