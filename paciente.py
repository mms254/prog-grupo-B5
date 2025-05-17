from typing import List
from persona import Persona
from citas import Cita
class Paciente(Persona):

    '''
    Clase que representa a un paciente en el sistema de gestión hospitalaria.

    Atributos
    ---------
    id : str
        Identificador único del paciente.
    username : str
        Nombre de usuario del paciente.
    password : str
        Contraseña del paciente.
    nombre : str
        Nombre del paciente.
    apellido : str
        Apellido del paciente.
    edad : int
        Edad del paciente.
    genero : str
        Género del paciente.
    estado : str
        Estado actual del paciente (grave, moderado, leve).
    medico_asignado : Medico, opcional
        Médico asignado al paciente.
    enfermero_asignado : Enfermero, opcional
        Enfermero asignado al paciente.
    habitacion_asginada : Habitacion, opcional
        Habitación asignada al paciente.
    enfermedades : List[str]
        Lista de enfermedades diagnosticadas al paciente.
    prioridad_urgencias : int
        Prioridad del paciente en urgencias (1: alta, 2: moderada, 3: baja).
    historial_medico : List[str]
        Historial médico del paciente.
    citas : List[Cita]
        Lista de citas del paciente.

    Métodos
    -------
    asignar_medico(medico: Medico) -> str
        Asigna un médico al paciente y devuelve un mensaje confirmando la asignación.

    asignar_habitacion(habitacion: Habitacion) -> str
        Asigna una habitación al paciente y devuelve un mensaje confirmando la asignación.

    asignar_enfermero(enfermero: Enfermero) -> str
        Asigna un enfermero al paciente y devuelve un mensaje confirmando la asignación.

    cambiar_estado(nuevo_estado: str) -> None
        Cambia el estado del paciente a un nuevo valor (grave, moderado, leve).

    prioridad_urgencias() -> None
        Establece la prioridad del paciente en urgencias según su estado (grave, moderado, leve).

    asignar_enfermedades(enfermedad: str) -> None
        Asigna una enfermedad al paciente si no está ya registrada en su historial.

    to_dict() -> dict
        Devuelve un diccionario con los atributos del paciente.
    '''

    # paciente.py
    class Paciente:
        def __init__(self, id, nombre, apellido, dni, telefono, email, direccion, historial_medico=None, citas=None,
                     estado="activo", medico_asignado=None, habitacion_asignada=None, rol="paciente"):
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.dni = dni  # <--- Asegúrate de que estos campos estén
            self.telefono = telefono  # <--- como parámetros en __init__
            self.email = email
            self.direccion = direccion
            self.historial_medico = historial_medico if historial_medico is not None else []
            self.citas = citas if citas is not None else []
            self.estado = estado
            self.medico_asignado = medico_asignado
            self.habitacion_asignada = habitacion_asignada
            self.rol = rol

        def __str__(self):
            return f"Paciente: {self.nombre} {self.apellido}"

    def asignar_medico(self, medico):
        '''
        Asigna un médico al paciente y devuelve un mensaje confirmando la asignación.

        Parámetros
        ----------
        medico : Medico
            Médico que se asignará al paciente.

        Devuelve
        --------
        str
            Mensaje que confirma la asignación del médico.
        '''
        self.medico_asignado = medico
        return f'El médico/a {medico.nombre} se ha asignado al paciente {self.nombre}'

    def asignar_habitacion(self, habitacion):
        '''
        Asigna una habitación al paciente y devuelve un mensaje confirmando la asignación.

        Parámetros
        ----------
        habitacion : Habitacion
            Habitación que se asignará al paciente.

        Devuelve
        --------
        str
            Mensaje que confirma la asignación de la habitación.
        '''
        self.habitacion_asginada = habitacion
        return f'Al paciente {self.nombre} se le ha asignado la habitación {habitacion.numero_habitacion}'

    def asignar_enfermero(self, enfermero):
        '''
        Asigna un enfermero al paciente y devuelve un mensaje confirmando la asignación.

        Parámetros
        ----------
        enfermero : Enfermero
            Enfermero que se asignará al paciente.

        Devuelve
        --------
        str
            Mensaje que confirma la asignación del enfermero.
        '''
        self.enfermero_asignado = enfermero
        return f'Al paciente {self.nombre} se le ha asignado el enfermero/a {enfermero.nombre}'

    def cambiar_estado(self, nuevo_estado):
        '''
        Cambia el estado del paciente a un nuevo valor (grave, moderado, leve).

        Parámetros
        ----------
        nuevo_estado : str
            Nuevo estado del paciente.
        '''
        self.estado = nuevo_estado

    def prioridad_urgencias(self):
        '''
        Establece la prioridad del paciente en urgencias según su estado (grave, moderado, leve).

        Devuelve
        --------
        None
            Modifica el valor de prioridad_urgencias en función del estado del paciente.
        '''
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
        '''
        Asigna una enfermedad al paciente si no está ya registrada en su historial.

        Parámetros
        ----------
        enfermedad : str
            Enfermedad que se asignará al paciente.

        Devuelve
        --------
        None
            Si la enfermedad ya está registrada, no se agrega nuevamente.
        '''
        if enfermedad not in self.enfermedades:
            self.enfermedades.append(enfermedad)
        else:
            print('El paciente ya tiene esa enfermedad')

    def to_dict(self): # Hecho por Ricardo
        '''
        Devuelve un diccionario con los atributos del paciente.

        Devuelve
        --------
        dict
            Diccionario con los atributos del paciente, incluyendo médicos, enfermeros, habitación y citas.
        '''
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'nombre': self.nombre,
            'edad': self.edad,
            'historial_medico': self.historial_medico,
            'citas': [cita.to_dict() for cita in self.citas],
            'rol': self.rol,
            'medico_asignado': self.medico_asignado,
            'prioridad_urgencias': self.prioridad_urgencias,
            'habitacion_asginada': self.habitacion_asginada,
            'estado': self.estado,
            'enfermero_asignado': self.enfermero_asignado.id if self.enfermero_asignado else None
        }

