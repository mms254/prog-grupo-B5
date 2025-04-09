from persona import Persona


class Paciente(Persona):
    '''
    Clase que representa a un paciente en el sistema hospitalario, con atributos como el estado de salud,
    médico asignado, habitación asignada, enfermedades y prioridad de urgencias.

    Atributos
    ----------
    id : str
        Identificador único del paciente.
    nombre : str
        Nombre del paciente.
    apellido : str
        Apellido del paciente.
    edad : int
        Edad del paciente.
    genero : str
        Género del paciente.
    estado : str
        Estado de salud del paciente (grave, moderado, leve).
    medico_asignado : Medico, opcional
        Médico asignado al paciente. Por defecto es None.
    habitacion_asginada : Habitacion, opcional
        Habitación asignada al paciente. Por defecto es None.
    enfermedades : list
        Lista de enfermedades diagnosticadas al paciente.
    enfermero_asignado : Enfermero, opcional
        Enfermero asignado al paciente. Por defecto es None.
    prioridad_urgencias : int
        Prioridad en urgencias basada en el estado de salud del paciente (1: alta, 2: moderada, 3: baja).

    Métodos
    -------
    __init__(id: str, nombre: str, apellido: str, edad: int, genero: str, estado: str, medico_asignado: Medico = None, habitacion_asginada: Habitacion = None)
        Inicializa los atributos del paciente.

    asignar_medico(medico: Medico) -> str
        Asigna un médico al paciente.

    asignar_habitacion(habitacion: Habitacion) -> str
        Asigna una habitación al paciente.

    asignar_enfermero(enfermero: Enfermero) -> str
        Asigna un enfermero al paciente.

    cambiar_estado(nuevo_estado: str)
        Cambia el estado de salud del paciente.

    prioridad_urgencias() -> None
        Establece la prioridad en urgencias según el estado de salud del paciente.

    asignar_enfermedades(enfermedad: str) -> None
        Asigna una enfermedad al paciente si no la tiene ya registrada.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, estado: str, medico_asignado=None,
                 habitacion_asginada=None, alergias: list = None) -> None:
        '''
        Inicializa los atributos del paciente.

        Parámetros
        ----------
        id : str
            Identificador único del paciente.
        nombre : str
            Nombre del paciente.
        apellido : str
            Apellido del paciente.
        edad : int
            Edad del paciente.
        genero : str
            Género del paciente.
        estado : str
            Estado de salud del paciente.
        medico_asignado : Medico, opcional
            Médico asignado al paciente. Por defecto es None.
        habitacion_asginada : Habitacion, opcional
            Habitación asignada al paciente. Por defecto es None.
        alergias: list, opcional
            Lista de alergias del paciente. Por defecto es None.
        '''
        super().__init__(id, nombre, apellido, edad, genero)
        self.estado = estado
        self.medico_asignado = medico_asignado
        self.habitacion_asignada = habitacion_asginada
        self.enfermedades = []
        self.enfermero_asignado = None
        self.prioridad_urgencias = 0
        if alergias is not None:
            self.alergias = alergias
        else:
            self.alergias = []

    def asignar_medico(self, medico) -> str:
        '''
        Asigna un médico al paciente.

        Parámetros
        ----------
        medico : Medico
            Médico que se asignará al paciente.

        Devuelve
        -------
        str
            Mensaje confirmando la asignación del médico al paciente.
        '''
        self.medico_asignado = medico
        return f'El médico/a {medico.nombre} se ha asignado al paciente {self.nombre}'

    def asignar_habitacion(self, habitacion) -> str:
        '''
        Asigna una habitación al paciente.

        Parámetros
        ----------
        habitacion : Habitacion
            Habitación que se asignará al paciente.

        Devuelve
        -------
        str
            Mensaje confirmando la asignación de la habitación al paciente.
        '''
        self.habitacion_asginada = habitacion
        return f'Al paciente {self.nombre} se le ha asignado la habitación {habitacion.numero_habitacion}'

    def asignar_enfermero(self, enfermero) -> str:
        '''
        Asigna un enfermero al paciente.

        Parámetros
        ----------
        enfermero : Enfermero
            Enfermero que se asignará al paciente.

        Devuelve
        -------
        str
            Mensaje confirmando la asignación del enfermero al paciente.
        '''
        self.enfermero_asignado = enfermero
        return f'Al paciente {self.nombre} se le ha asignado el enfermero/a {enfermero.nombre}'

    def cambiar_estado(self, nuevo_estado: str) -> None:
        '''
        Cambia el estado de salud del paciente.

        Parámetros
        ----------
        nuevo_estado : str
            Nuevo estado de salud del paciente (grave, moderado, leve).
        '''
        self.estado = nuevo_estado

    def prioridad_urgencias(self) -> None:
        '''
        Establece la prioridad en urgencias según el estado de salud del paciente.

        Devuelve
        -------
        None
            Establece la prioridad de urgencias.
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

    def asignar_enfermedades(self, enfermedad: str) -> None:
        '''
        Asigna una enfermedad al paciente si no la tiene ya registrada.

        Parámetros
        ----------
        enfermedad : str
            Nombre de la enfermedad que se asignará al paciente.

        Excepciones
        ------------
        ValueError
            Si el paciente ya tiene esa enfermedad asignada.
        '''
        if enfermedad not in self.enfermedades:
            self.enfermedades.append(enfermedad)
        else:
            print('El paciente ya tiene esa enfermedad asignada.')


# Creación de objetos de la clase Paciente
paciente1 = Paciente(id='P001', nombre='Carlos', apellido='Crespo', edad=45, genero='Masculino', estado='grave')
paciente2 = Paciente(id="P002", nombre='Lucia', apellido='Monteagudo', edad=36, genero='Femenino', estado='moderado')
paciente3 = Paciente(id="P003", nombre='Marcos', apellido='Hernandez', edad=60, genero='Masculino', estado='leve')
paciente4 = Paciente(id="P004", nombre='Daniel', apellido='Paredes', edad=52, genero='Masculino', estado='grave')
paciente5 = Paciente(id="P005", nombre='Mario', apellido='Morant', edad=28, genero='Masculino', estado='moderado')
paciente6 = Paciente(id="P006", nombre='Pedro', apellido='Sánchez', edad=39, genero='Masculino', estado='leve')
paciente7 = Paciente(id="P007", nombre='Tralalero', apellido='Tralala', edad=48, genero='Masculino', estado='grave')
paciente8 = Paciente(id="P008", nombre='David', apellido='Díez', edad=31, genero='Masculino', estado='moderado')
paciente9 = Paciente(id="P009", nombre='Ester', apellido='Estirado', edad=55, genero='Femenino', estado='leve')
paciente10 = Paciente(id="P010", nombre='Tung Tung', apellido='Sahur', edad=40, genero='Masculino', estado='grave')
paciente11 = Paciente(id='P011', nombre='Natalia Sofia', apellido='Vila', edad=69, genero='Femenino', estado='moderado')
