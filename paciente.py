# paciente.py

from persona import Persona

class Paciente(Persona):
    def __init__(self, id, nombre, apellido, edad, genero, estado, medico_asignado=None, alergias=None, habitacion_asignada=None):
        super().__init__(id, nombre, apellido, edad, genero)
        self.estado = estado
        self.medico_asignado = medico_asignado
        self.alergias = alergias if alergias else []  # Lista de alergias
        self.habitacion_asignada = habitacion_asignada

    # Método para cambiar el estado del paciente
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f'El estado del paciente {self.nombre} ha sido cambiado a {self.estado}.')

    # Asignar alergias al paciente
    def asignar_alergias(self, alergias):
        self.alergias = alergias
        print(f'Las alergias del paciente {self.nombre} han sido actualizadas.')

    # Asignar médico al paciente
    def asignar_medico(self, medico):
        self.medico_asignado = medico

    # Asignar habitación al paciente
    def asignar_habitacion(self, habitacion):
        self.habitacion_asignada = habitacion

    def __str__(self):
        return f'{self.nombre} {self.apellido}, Estado: {self.estado}, Alergias: {self.alergias}, Médico: {self.medico_asignado.nombre if self.medico_asignado else "No asignado"}'
