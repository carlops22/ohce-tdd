import datetime
import sys
class Ohce:
    def __init__(self,name):
        self.name = name

    def get_current_hour():
        now = datetime.datetime.now()
        current_hour = now.hour
        return current_hour
    @staticmethod   
    def get_greeting(current_hour=None):
        if current_hour is None:
            current_hour= Ohce.get_current_hour()
        if not (0 <= current_hour < 24):
            raise ValueError("Invalid hour")
        if 6 <= current_hour < 12:
            return "¡Buenos días"
        elif 12 <= current_hour < 20:
            return "¡Buenas tardes"
        else:
            return "¡Buenas noches"

    def return_greeting(self, current_hour= None):
        greeting = self.get_greeting(current_hour)
        return f"{greeting} {self.name}!"
    def ohce(self, input, output_f):
        output_f(self.return_greeting()) 
        while True:
            user_input = input("> ")
            if user_input == "Stop!":
                output_f(f"Adios {self.name}")
                break



        
    