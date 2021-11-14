import os
import requests
from PIL import Image
from pyzbar.pyzbar import decode
for root, dirs, files in os.walk('./downloads'):
     for file in files:
        try:
            data = decode(Image.open(root+"/"+file))
            print(data[0].data.decode('UTF-8')[43:])
            id_hash = data[0].data.decode('UTF-8')[43:]
            final_url = "https://www.gosuslugi.ru/api/covid-cert/v3/cert/check/"+id_hash
            r = requests.get(final_url)
            print(r.text)
            with open("resp_text.html", "w") as file:
                file.write(r.text)
        except Exception:
            print("QR decode error")




