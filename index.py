import calendar
from datetime import date, datetime

agnio = int (input(' Digita el año: '))

mes = int (input(' Digite el mes: '))

estaciones = input(" Digite la estacion de ese mes o la que dese: ")



print (calendar.month(agnio,mes))

if(estaciones == "12" or estaciones == "1" or estaciones == "2" ):
    print(f" El mes {estaciones} esta en INVIERNO")

if(estaciones == "3" or estaciones == "4" or estaciones == "5" ):
    print(f" El mes {estaciones} esta en PRIMAVERA")

if(estaciones == "6" or estaciones == "7" or estaciones == "8" ):
    print(f" El mes {estaciones} esta en VERANO")

if(estaciones == "9" or estaciones == "10" or estaciones == "11" ):
    print(f" El mes {estaciones} esta en OTOÑO")







