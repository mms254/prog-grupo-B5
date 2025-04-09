from persona import Persona

class Paciente(Persona):
    def __init__(self, id, nombre, apellido, edad, genero, estado, medico_asignado=None, habitacion_asginada = None):
        super().__init__(id, nombre, apellido, edad, genero)
        self.estado = estado
        self.medico_asignado = medico_asignado
        self.habitacion_asginada = habitacion_asginada
        self.enfermedades = []
        self.prioridad_urgencias = 0
    def asignar_medico(self, medico):
        self.medico_asignado = medico
        return f'El médico/a {medico.nombre} se ha asignado al paciente {self.nombre}'
    def asignar_habitacion(self, habitacion):
        self.habitacion_asignada = habitacion
        return f'Al paciente {self.nombre} se le ha asignado la habitacion {habitacion.numero_habitacion}'
    def asignar_enfermero(self, enfermero):
        self.enfermero_asignado = enfermero
        return f'Al paciente {self.nombre} se le ha asignado el enfermero/a {enfermero.nombre}'
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    def prioridad_urgencias(self):
        if self.estado.lower() == 'grave':
            self.prioridad_urgencias = 1
            print(f'El paciente {self.nombre} tiene prioridad alta en urgencias.')
        elif self.estado.lower() == 'moderado':
            self.prioridad_urgencias = 2
            print(f'El paciente {self.nombre} tiene prioridad moderada en urgencias.')
        elif self.estado.lower() == 'leve':
            self.prioridad_urgencias = 3
            print(f'El paciente {self.nombre} tiene prioridad baja en urgencias.')
    def asignar_enfermedades(self, enfermedad):
        if enfermedad not in self.enfermedades:
            self.enfermedades.append(enfermedad)
        else:
            print('El paciente ya tiene esa enfermedad')