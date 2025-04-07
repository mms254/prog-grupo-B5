from persona import Persona

class Paciente(Persona):
    def __init__(self, id, nombre, apellido, edad, genero, estado, medico_asignado=None):
        super().__init__(id, nombre, apellido, edad, genero)
        self.estado = estado
        self.medico_asignado = medico_asignado