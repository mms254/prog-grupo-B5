from trabajador import Trabajador

class Paramedico(Trabajador):
    '''
    Clase que representa a un paramédico dentro del sistema hospitalario. Hereda de la clase Trabajador
    y extiende con atributos específicos como especialidad, antigüedad y ambulancia asignada.

    Atributos
    ----------
    id : str
        Identificador único del paramédico.
    nombre : str
        Nombre del paramédico.
    apellido : str
        Apellido del paramédico.
    edad : int
        Edad del paramédico.
    genero : str
        Género del paramédico.
    turno : str
        Turno de trabajo del paramédico (mañana, tarde, noche).
    horas : int
        Número de horas de trabajo semanales del paramédico.
    salario : float
        Salario del paramédico.
    especialidad : str
        Especialidad del paramédico (por ejemplo, Emergencias, Cardiología, etc.).
    antiguedad : int
        Antigüedad del paramédico en años.
    ambulancia_asignada : Ambulancia, opcional
        Ambulancia asignada al paramédico. Por defecto es None.

    Métodos
    -------
    __init__(id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, especialidad: str, antiguedad: int)
        Inicializa los atributos del paramédico, incluyendo validación del id.

    asignar_ambulancia(ambulancia: Ambulancia) -> None
        Asigna una ambulancia al paramédico, asegurándose de que no esté asignado a otra.

    __str__() -> str
        Retorna una cadena con los detalles del paramédico, incluyendo la ambulancia asignada si la tiene.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int,
                 salario: float, especialidad: str, antiguedad: int) -> None:
        '''
        Inicializa los atributos del paramédico, asegurándose de que el id comience con 'PAR'.

        Parámetros
        ----------
        id : str
            Identificador único del paramédico.
        nombre : str
            Nombre del paramédico.
        apellido : str
            Apellido del paramédico.
        edad : int
            Edad del paramédico.
        genero : str
            Género del paramédico.
        turno : str
            Turno de trabajo del paramédico (mañana, tarde, noche).
        horas : int
            Número de horas de trabajo semanales del paramédico.
        salario : float
            Salario del paramédico.
        especialidad : str
            Especialidad del paramédico (por ejemplo, Emergencias, Cardiología, etc.).
        antiguedad : int
            Antigüedad del paramédico en años.

        Excepciones
        ------------
        ValueError
            Si el id no empieza con 'PAR'.
        '''
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.ambulancia_asignada = None
        if not id.startswith('PAR'):
            raise ValueError('Has insertado un id inválido, debe empezar por PAR')

    def asignar_ambulancia(self, ambulancia) -> None:
        '''
        Asigna una ambulancia al paramédico si no está asignado a otra.

        Parámetros
        ----------
        ambulancia : Ambulancia
            Ambulancia que se asignará al paramédico.

        Excepciones
        ------------
        ValueError
            Si el paramédico ya está asignado a una ambulancia.
        '''
        if self.ambulancia_asignada is not None:
            raise ValueError(f'El paramédico {self.nombre} ya está asignado a una ambulancia.')
        self.ambulancia_asignada = ambulancia
        ambulancia.asignar_paramedico(self)

    def __str__(self) -> str:
        '''
        Devuelve una cadena con los detalles del paramédico, incluyendo la ambulancia asignada si la tiene.

        Devuelve
        -------
        str
            Información detallada sobre el paramédico, incluyendo la ambulancia asignada si existe.
        '''
        if self.ambulancia_asignada is not None:
            return (
                f'Nombre: {self.nombre} - ID: {self.id} - Edad: {self.edad} - Género: {self.genero} - Turno: {self.turno} - Horas: {self.horas} - '
                f' Salario: {self.salario} - Especialidad: {self.especialidad} - Antiguedad: {self.antiguedad} - Ambulancia: {self.ambulancia_asignada.matricula}')
        else:
            return (f'Nombre: {self.nombre} - ID: {self.id} - Edad: {self.edad} - Género: {self.genero} - '
                    f'Turno: {self.turno} - Horas: {self.horas} - Salario: {self.salario} - '
                    f'Especialidad: {self.especialidad} - Antigüedad: {self.antiguedad} - '
                    f'Ambulancia: No asignada')


# Creación de objetos de la clase Paramedico
paramedico1 = Paramedico(
    id='PAR001',
    nombre='Laura',
    apellido='Gómez',
    edad=32,
    genero='Femenino',
    turno='mañana',
    horas=36,
    salario=1600,
    especialidad='Emergencias',
    antiguedad=4
)

paramedico2 = Paramedico(
    id='PAR002',
    nombre='Andrés',
    apellido='Martínez',
    edad=45,
    genero='Masculino',
    turno='tarde',
    horas=40,
    salario=1700,
    especialidad='Traumatología',
    antiguedad=10
)

paramedico3 = Paramedico(
    id='PAR003',
    nombre='Carmen',
    apellido='López',
    edad=29,
    genero='Femenino',
    turno='noche',
    horas=38,
    salario=1650,
    especialidad='Cardiología',
    antiguedad=6
)

paramedico4 = Paramedico(
    id='PAR004',
    nombre='Jorge',
    apellido='Ruiz',
    edad=39,
    genero='Masculino',
    turno='mañana',
    horas=35,
    salario=1550,
    especialidad='Pediatría',
    antiguedad=3
)

paramedico5 = Paramedico(
    id='PAR005',
    nombre='Natalia',
    apellido='Fernández',
    edad=41,
    genero='Femenino',
    turno='tarde',
    horas=37,
    salario=1680,
    especialidad='Cuidados intensivos',
    antiguedad=8
)
