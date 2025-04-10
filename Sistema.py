# sistema_prosalud.py
from ManejoHabitaciones import ManejoHabitaciones

class SistemaProSalud:
    def __init__(self):
        self.personas = {}  # Diccionario para almacenar personas: {username: Persona}
        self.manejo_habitaciones = ManejoHabitaciones()

    def agregar_persona(self, persona):
        if persona.username in self.personas:
            raise ValueError(f"El usuario {persona.username} ya existe")
        self.personas[persona.username] = persona

    def buscar_persona(self, username):
        return self.personas.get(username)