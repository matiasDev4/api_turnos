import datetime
from datetime import time, date, timedelta
import os
import json
import locale


# Crear clase fecha
# Crear clase hora
path = os.getcwd() 

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def crear_fecha() -> list:
    dateList = []
    today = datetime.date.today()

    year_end = datetime.date(today.year, 12, 31)

    while today <= year_end:
        today += datetime.timedelta(days=1)
        dateList.append(today.strftime("%d-%m-%Y"))
    return dateList

        
        