# gestion_usuarios.py

from medico import Medico
from enfermero import Enfermero
from auxiliar import Auxiliar
from paciente import Paciente
from habitacion import Habitacion

class GestionUsuarios:
    def __init__(self):
        # Diccionarios para almacenar usuarios
        self.pacientes = {}
        self.medicos = {}
        self.enfermeros = {}
        self.auxiliares = {}

    # Alta de paciente
    def alta_paciente(self, paciente):
        self.pacientes[paciente.id] = paciente
        print(f'Paciente {paciente.nombre} {paciente.apellido} dado de alta.')

    # Baja de paciente
    def baja_paciente(self, id_paciente):
        if id_paciente in self.pacientes:
            del self.pacientes[id_paciente]
            print(f'Paciente con ID {id_paciente} dado de baja.')
        else:
            print(f'No se encontró al paciente con ID {id_paciente}.')

    # Alta de trabajador (médico, enfermero, auxiliar)
    def alta_trabajador(self, trabajador):
        if isinstance(trabajador, Medico):
            self.medicos[trabajador.id] = trabajador
        elif isinstance(trabajador, Enfermero):
            self.enfermeros[trabajador.id] = trabajador
        elif isinstance(trabajador, Auxiliar):
            self.auxiliares[trabajador.id] = trabajador
        print(f'Trabajador {trabajador.nombre} {trabajador.apellido} dado de alta.')

    # Baja de trabajador
    def baja_trabajador(self, id_trabajador):
        if id_trabajador in self.medicos:
            del self.medicos[id_trabajador]
        elif id_trabajador in self.enfermeros:
            del self.enfermeros[id_trabajador]
        elif id_trabajador in self.auxiliares:
            del self.auxiliares[id_trabajador]
        print(f'Trabajador con ID {id_trabajador} dado de baja.')

    # Asignar médico a paciente
    def asignar_medico_paciente(self, paciente, medico):
        paciente.medico_asignado = medico
        print(f'Paciente {paciente.nombre} asignado a médico {medico.nombre}.')

    # Asignar habitación a paciente
    def asignar_habitacion_paciente(self, paciente, habitacion):
        paciente.habitacion_asignada = habitacion
        print(f'Paciente {paciente.nombre} asignado a la habitación {habitacion.numero}.')

    # Mostrar pacientes activos
    def listar_pacientes(self):
        print("Pacientes Activos:")
        for paciente in self.pacientes.values():
            print(f'{paciente.nombre} {paciente.apellido} - Estado: {paciente.estado} - Médico Asignado: {paciente.medico_asignado.nombre if paciente.medico_asignado else "No asignado"}')

    # Mostrar trabajadores
    def listar_trabajadores(self):
        print("Médicos:")
        for medico in self.medicos.values():
            print(medico)
        print("Enfermeros:")
        for enfermero in self.enfermeros.values():
            print(enfermero)
        print("Auxiliares:")
        for auxiliar in self.auxiliares.values():
            print(auxiliar)

