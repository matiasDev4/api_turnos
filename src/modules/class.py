import datetime
from datetime import time, date
import os
import json

# Crear clase fecha
# Crear clase hora
path = os.getcwd() 

class Date:
    def __init__(self, date1: datetime.datetime, date2: datetime.datetime, hour1: datetime.time, hour2: datetime.time, name: str):
        self.date1 = date1
        self.date2 = date2
        self.dateList = []
        self.hour1 = hour1
        self.hour2 = hour2
        self.hourList = []
        self.name = name
        self.data = {"months": []}
        self.data["months"] = [{self.name: []}]
         
    
    def create_date(self):
        
        #Funcion para crear las fechas - almacenarlas en un array 
        #El usuario puede generar un rango de fechas a eleccion
        #Asignar un minimo de 5 horarios distintos por fecha

        if self.dateList == []: #-< Si el array esta vacio
            while self.date1 <= self.date2: #-> Mientras la fecha 1 sea menor o igual a la fecha 2
                if self.date1.weekday() < 5 and self.date1.weekday() != 0: #-> Salteo de dias lunes, Sabados y Domingos
                    self.dateList.append(self.date1.strftime("%a-%m-%Y")) #-> Agrego las fechas al array
                self.date1 = self.date1 + datetime.timedelta(days=1) #-> Sumo un dia a la fecha
            #return self.dateList
        
        if self.hourList == []:
            while self.hour1 <= self.hour2:
                self.hourList.append(self.hour1.strftime("%H:%M:%S"))
                self.hour1 = (datetime.datetime.combine(date.today(), self.hour1) + datetime.timedelta(minutes=60)).time()
            #return self.hourList
        
        if not os.path.exists(path + "/dates"):
            os.makedirs(path + "/dates")

        if not os.path.exists(path + "/dates/dates.json"):
            with open (path + "/dates/dates.json", "w") as file:
                for list_data in self.dateList:
                    self.data["months"][0][{f"date":list_data, "hour": [str(x) for x in self.hourList]}]
                data_json = json.dumps(self.data, indent=4)
                file.write(data_json)   

        if os.path.exists(path + "/dates/dates.json"):
            with open (path + "/dates/dates.json") as file:
                json_file = json.load(file)
                for list_data in self.dateList:
                    json_file["months"][0].append({f"date":list_data, "hour": [str(x) for x in self.hourList]})

            with open (path + "/dates/dates.json", "w") as outfile:

                json.dump(json_file, outfile, indent=4)

            return "Archivo creado con exito"
        

    
print(Date(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 31), datetime.time(8, 0, 0), datetime.time(18, 0, 0), "Mes enero").create_date())
print(Date(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 31), datetime.time(8, 0, 0), datetime.time(18, 0, 0), "Mes febrero").create_date())


