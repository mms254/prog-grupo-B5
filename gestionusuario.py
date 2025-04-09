# gestion_usuarios.py
# importamos las clases necesarias para gestionar usuarios:
# médico, enfermero y auxiliar, son tipos de trabajadores del sistema
# paciente, aquellos que reciben atención médica
# habitaciones, a las que se le pueden asignar pacientes

from medico import Medico
from enfermero import Enfermero
from auxiliar import Auxiliar
from paciente import Paciente
from habitacion import Habitacion

# en esta clase nos encargamos de gestionar el alta, la baja
# asignamos a todos los usuarios del sistema hospitalario(pacientes y trabajadores)
# es una clase gestora
class GestionUsuarios:
    def __init__(self):
        # Diccionarios para almacenar usuarios
        # lo almacenamos según sea su tipo
        # usamos el id de cada persona como clave del diccionario
        self.pacientes = {}
        self.medicos = {}
        self.enfermeros = {}
        self.auxiliares = {}

    # Alta de paciente:
    # 1) recibe un objeto paciente
    # 2) lo guarda en el diccionario self.pacientes
    # 3) imprime un mensaje donde confirmamos el alta del paciente
    def alta_paciente(self, paciente):
        self.pacientes[paciente.id] = paciente
        print(f'Paciente {paciente.nombre} {paciente.apellido} dado de alta.')

    # Baja de paciente:
    # eliminamos a un paciente del sistema mediante el id, al darlo de baja
    # si ese paciente no se encuentra mostramos un mensaje de error
    def baja_paciente(self, id_paciente):
        if id_paciente in self.pacientes:
            del self.pacientes[id_paciente]
            print(f'Paciente con ID {id_paciente} dado de baja.')
        else:
            print(f'No se encontró al paciente con ID {id_paciente}.')

    # Alta de trabajador (médico, enfermero, auxiliar)
    # recibe un objeto que puede ser o médico o enfermero o auxiliar
    # depende del tipo lo guarda en cada diccionario al que corresponda
    # imprime la confirmación del alta

    def alta_trabajador(self, trabajador):
        if isinstance(trabajador, Medico):
            self.medicos[trabajador.id] = trabajador
        elif isinstance(trabajador, Enfermero):
            self.enfermeros[trabajador.id] = trabajador
        elif isinstance(trabajador, Auxiliar):
            self.auxiliares[trabajador.id] = trabajador
        print(f'Trabajador {trabajador.nombre} {trabajador.apellido} dado de alta.')

    # Baja de trabajador:
    # elimina al trabajador(médico,enfermero o auxiliar) según su id
    # lo busca en cada diccionario y lo borra si está
    # imprime un mensaje de confirmación

    def baja_trabajador(self, id_trabajador):
        if id_trabajador in self.medicos:
            del self.medicos[id_trabajador]
        elif id_trabajador in self.enfermeros:
            del self.enfermeros[id_trabajador]
        elif id_trabajador in self.auxiliares:
            del self.auxiliares[id_trabajador]
        print(f'Trabajador con ID {id_trabajador} dado de baja.')

    # Asignar médico a paciente:
    # asocia un médico a un paciente
    # se asigna el objeto médico al atributo medico_asignado del paciente
    # muestra un mensaje de confirmación

    def asignar_medico_paciente(self, paciente, medico):
        paciente.medico_asignado = medico
        print(f'Paciente {paciente.nombre} asignado a médico {medico.nombre}.')

    # Asignar habitación a paciente:
    # asigna una habitación al paciente
    # el objeto habitación se guarda en el atributo habitacion_asignado
    # imprime el número de habitación asignado

    def asignar_habitacion_paciente(self, paciente, habitacion):
        paciente.habitacion_asignada = habitacion
        print(f'Paciente {paciente.nombre} asignado a la habitación {habitacion.numero}.')

    # Mostrar pacientes activos:
    # muestra por pantalla todos los pacientes activos
    # imprimimos su nombre, estado y nombre deel médico asignado si lo tiene

    def listar_pacientes(self):
        print("Pacientes Activos:")
        for paciente in self.pacientes.values():
            print(f'{paciente.nombre} {paciente.apellido} - Estado: {paciente.estado} - Médico Asignado: {paciente.medico_asignado.nombre if paciente.medico_asignado else "No asignado"}')

    # Mostrar trabajadores:
    # muestra a todos los trabajadores activos clasificados por rol
    # llamamos al método __str__() de cada clase para imprimir sus datos

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

