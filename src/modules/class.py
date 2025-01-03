import datetime, time

# Crear clase fecha
# Crear clase hora

class date_():
    def __init__(self, date: datetime):
        self.date = date
    
    
    def create_date(self):
        #Funcion para crear las fechas - almacenarlas en un array 
        self.date_list = []
        self.date_list.append(self.date)
        return self.date_list

class hours():
    def __init__(self, hour: time):
        self.hour = hour
    
    def create_hour(self):
        #Funcion para crear las horas - almacenarlas en un array 
        self.hour_list = []
        self.hour_list.append(self.hour)
        return self.hour_list

