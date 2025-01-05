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
    def __init__(self, date1: datetime.datetime, date2: datetime.datetime, hour1: datetime.time, hour2: datetime.time, name: str):
        self.date1 = date1
        self.date2 = date2
        self.dateList = []
        self.hour1 = hour1
        self.hour2 = hour2
        self.hourList = []
        self.name = name
        self.data = {"dates": []}

    
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
                self.hourList.append(self.hour1.strftime("%H:%M:%S"))
                self.hour1 = (datetime.datetime.combine(date.today(), self.hour1) + datetime.timedelta(minutes=60)).time()
            #return self.hourList
        
        if not os.path.exists(path + "/dates"):
            os.makedirs(path + "/dates")

        json_path = path + "/dates/dates.json"

        if os.path.exists(json_path):
            with open (json_path, "r", encoding="utf-8") as file:
                json_file = json.load(file)
                
        else:
            json_file = {"dates": []}

        new = {
                "months": self.name, 
                "date": [str(x) for x in self.dateList], 
                "hour":[str(x) for x in self.hourList]
            }

        if not any(d['date'] == new['date'] for d in json_file["dates"]):
            json_file["dates"].append(new)
                    
        with open (json_path, "w", encoding="utf-8") as outfile:
            json.dump(json_file, outfile, indent=4)

        return "Archivo creado con exito"
        

    
print(Date(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 31), datetime.time(8, 0, 0), datetime.time(18, 0, 0), "Enero").create_date())
print(Date(datetime.datetime(2021, 2, 1), datetime.datetime(2021, 2, 28), datetime.time(8, 0, 0), datetime.time(18, 0, 0), "Febrero").create_date())
