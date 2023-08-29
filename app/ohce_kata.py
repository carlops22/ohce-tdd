import datetime
def get_current_hour():
    now = datetime.datetime.now()
    current_hour = now.hour
    return current_hour
class Ohce:
    def __init__(self,name):
        self.name = name
    
    def get_greeting(self):
        current_hour= get_current_hour()
        if 20 <= current_hour <6:
            return "¡Buenas noches"
        elif 6 <= current_hour <12:
            return "¡Buenos días"
        else:
            return "¡Buenas tardes"

    def return_greeting(self):
        greeting = self.get_greeting()
        return f"{greeting} {self.name}!"
    