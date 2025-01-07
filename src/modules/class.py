import datetime
from datetime import time, date
import os
import json
import locale

# Crear clase fecha
# Crear clase hora
path = os.getcwd() 

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Date:
    def __init__(self, date1: datetime.datetime, date2: datetime.datetime, hour1: datetime.time, hour2: datetime.time):
        self.date1 = date1
        self.date2 = date2
        self.dateList = []
        self.hour1 = hour1
        self.hour2 = hour2
        self.hourList = []

    
    def create_date(self):
        
        #Funcion para crear las fechas - almacenarlas en un array 
        #El usuario puede generar un rango de fechas a eleccion
        #Asignar un minimo de 5 horarios distintos por fecha

        if self.dateList == []: #-< Si el array esta vacio
            while self.date1 <= self.date2: #-> Mientras la fecha 1 sea menor o igual a la fecha 2
                if self.date1.weekday() < 5 and self.date1.weekday() != 0: #-> Salteo de dias lunes, Sabados y Domingos
                    self.dateList.append(self.date1.strftime("%a | %d-%m-%Y")) #-> Agrego las fechas al array
                self.date1 = self.date1 + datetime.timedelta(days=1) #-> Sumo un dia a la fecha
            #return self.dateList
        
        if self.hourList == []:
            while self.hour1 <= self.hour2:
                self.hourList.append(self.hour1.strftime("%H:%M"))
                self.hour1 = (datetime.datetime.combine(date.today(), self.hour1) + datetime.timedelta(minutes=60)).time()
            #return self.hourList
        
        
