# paciente.py
# importamos la clase persona, que será la clase base desde la cual hereda paciente
from persona import Persona
# paciente hereda de persona, por lo tanto, tendrá todos los atributos como id
# nombre,apellido, edad rango y género y le añadimos nuevos atributos específicos para pacientes

class Paciente(Persona):
    # se llama al constructor de persona para inicializar los atributos
    # comunes id, nombre, apellido, edad, genero
    # luego inicializo nuevos atributos propios de un paciente
    def __init__(self, id, nombre, apellido, edad, genero, estado, medico_asignado=None, alergias=None, habitacion_asignada=None):
        super().__init__(id, nombre, apellido, edad, genero)
        self.estado = estado
        self.medico_asignado = medico_asignado
        self.alergias = alergias if alergias else []  # Lista de alergias
        self.habitacion_asignada = habitacion_asignada

    # Método para cambiar el estado del paciente
    # cambia el estado actual del paciente
    # imprimimos un mensaje informativo
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f'El estado del paciente {self.nombre} ha sido cambiado a {self.estado}.')

    # Asignar alergias al paciente
    # permite asignar o actualizar la lista de alergias del paciente
    # aceptando así una lista de strings, como 'penicilina' o 'polen'
    def asignar_alergias(self, alergias):
        self.alergias = alergias
        print(f'Las alergias del paciente {self.nombre} han sido actualizadas.')

    # Asignar médico al paciente
    # asignamos un objeto médico al paciente
    # no imprimimos ningún mensaje
    def asignar_medico(self, medico):
        self.medico_asignado = medico

    # Asignar habitación al paciente
    # para ello asiganamos un objeto habitacion al paciente
    def asignar_habitacion(self, habitacion):
        self.habitacion_asignada = habitacion
    # este método define cómo imprimir un paciente
    # incluyendo:
    # nombre completo, estado, alergias o el medico asignado si lo hay
    def __str__(self):
        return f'{self.nombre} {self.apellido}, Estado: {self.estado}, Alergias: {self.alergias}, Médico: {self.medico_asignado.nombre if self.medico_asignado else "No asignado"}'
