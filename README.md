**** Не релевантно тк всех вылечили события после 24.02.2022

Поиск QR кодов вакциинации находящихся в свободном доступе в Google поисковике
######################

Скрипт информация по каждому найденому qr коду в базу данных

Пререквизиты:

```
brew install zbar
brew install postgresql
brew install virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install psycopg2
pip install pillow
pip install pyzbar
```
Создать базу
```
createdb qr
```

Запуск
1. Скачиваем QR картинки
```
cd qr
python qr/qr.py
```
2. Запускам сканер и делаем запросы на госуслуги по каждому из скачанных qr кодов
```
cd qr
python qr/check.py
```
Disclaimer
==========

Прогмамма создана в ознакомительных целях для всеобщего блага.

Please do not download or use any image that violates its copyright terms.
Google Images is a search engine that merely indexes images and allows you to find them.
It does NOT produce its own images and, as such, it doesn't own copyright on any of them.
The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners,
even if they do not explicitly carry a copyright warning.
You may not reproduce copyright images without their owner'self permission,
except in "fair use" cases,
or you could risk running into lawyer'self warnings, cease-and-desist letters, and copyright suits.
Please be very careful before its usage! Use this script/code only for educational purposes.
