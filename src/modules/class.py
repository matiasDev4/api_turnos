import datetime
from datetime import time, date

# Crear clase fecha
# Crear clase hora

class Date:
    def __init__(self, date1: datetime.datetime, date2: datetime.datetime):
        self.date1 = date1
        self.date2 = date2
        self.dateList = []
    
    def create_date(self):
        
        #Funcion para crear las fechas - almacenarlas en un array 
        #El usuario puede generar un rango de fechas a eleccion
        #Asignar un minimo de 5 horarios distintos por fecha

        if self.dateList == []: #-< Si el array esta vacio
            while self.date1 <= self.date2: #-> Mientras la fecha 1 sea menor o igual a la fecha 2
                if self.date1.weekday() < 5 and self.date1.weekday() != 0: #-> Salteo de dias lunes, Sabados y Domingos
                    self.dateList.append(self.date1.strftime("%d-%m-%Y")) #-> Agrego las fechas al array
                self.date1 = self.date1 + datetime.timedelta(days=1) #-> Sumo un dia a la fecha
            return self.dateList


print(Date(datetime.datetime(2021, 1, 1), datetime.datetime(2021, 2, 1)).create_date())


