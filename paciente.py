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

    def __init__(self, id, username, password, nombre, apellido, edad, genero, estado, medico_asignado=None,
                 enfermero_asignado=None, habitacion_asginada=None, historial_medico: List[str] = None):
        super().__init__(id, nombre, apellido, edad, genero)
        self.username = username
        self.password = password
        self.estado = estado
        self.medico_asignado = medico_asignado
        self.enfermero_asignado = enfermero_asignado
        self.habitacion_asginada = habitacion_asginada
        self.enfermedades = []
        self.prioridad_urgencias = 0
        self.historial_medico = historial_medico if historial_medico is not None else []
        self.citas: List[Cita] = []

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

# Creación de objetos de la clase Paciente
paciente1 = Paciente(id='P001', username='carlos_crespo', password='password123', nombre='Carlos', apellido='Crespo', edad=45, genero='Masculino', estado='grave', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente2 = Paciente(id="P002", username='lucia_monteagudo', password='password123', nombre='Lucia', apellido='Monteagudo', edad=36, genero='Femenino', estado='moderado', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente3 = Paciente(id="P003", username='marcos_hernandez', password='password123', nombre='Marcos', apellido='Hernandez', edad=60, genero='Masculino', estado='leve', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente4 = Paciente(id="P004", username='daniel_paredes', password='password123', nombre='Daniel', apellido='Paredes', edad=52, genero='Masculino', estado='grave', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente5 = Paciente(id="P005", username='mario_morant', password='password123', nombre='Mario', apellido='Morant', edad=28, genero='Masculino', estado='moderado', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente6 = Paciente(id="P006", username='pedro_sanchez', password='password123', nombre='Pedro', apellido='Sánchez', edad=39, genero='Masculino', estado='leve', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente7 = Paciente(id="P007", username='tralalero_tralala', password='password123', nombre='Tralalero', apellido='Tralala', edad=48, genero='Masculino', estado='grave', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente8 = Paciente(id="P008", username='david_diez', password='password123', nombre='David', apellido='Díez', edad=31, genero='Masculino', estado='moderado', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente9 = Paciente(id="P009", username='ester_estirado', password='password123', nombre='Ester', apellido='Estirado', edad=55, genero='Femenino', estado='leve', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente10 = Paciente(id="P010", username='tung_tung_sahur', password='password123', nombre='Tung Tung', apellido='Sahur', edad=40, genero='Masculino', estado='grave', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
paciente11 = Paciente(id='P011', username='natalia_sofia_vila', password='password123', nombre='Natalia Sofia', apellido='Vila', edad=69, genero='Femenino', estado='moderado', medico_asignado=None, enfermero_asignado=None, habitacion_asginada=None, historial_medico=[])
