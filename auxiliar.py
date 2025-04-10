from enfermero import enfermero1
from enfermero import enfermero5
from enfermero import enfermero3
from trabajador import Trabajador

class Auxiliar(Trabajador):
    '''
    Clase que representa un auxiliar en el sistema hospitalario.
    Hereda de la clase `Trabajador`.

    Atributos
    ----------
    id : str
        Identificador único del auxiliar. Debe empezar por 'AUX'.
    nombre : str
        Nombre del auxiliar.
    apellido : str
        Apellido del auxiliar.
    edad : int
        Edad del auxiliar.
    genero : str
        Género del auxiliar.
    turno : str
        Turno asignado al auxiliar (mañana, tarde, noche).
    horas : int
        Número de horas trabajadas semanalmente.
    salario : float
        Salario base del auxiliar, ajustado según antigüedad y turno.
    enfermero_asignado : object or None
        Enfermero asignado al auxiliar. Puede ser un objeto de la clase `Enfermero`.
    antiguedad : int
        Antigüedad del auxiliar en años.

    Métodos
    -------
    __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, enfermero_asignado, antiguedad)
        Inicializa una nueva instancia de `Auxiliar`.

    calculo_salario(self) -> float
        Calcula y devuelve el salario del auxiliar según su antigüedad y turno.

    limpiar_habitacion(self, habitaciones) -> list
        Limpia las habitaciones que no están limpias y devuelve una lista de las habitaciones que han sido limpiadas.

    asignar_enfermero(self, enfermero) -> None
        Asigna un enfermero al auxiliar, si no tiene uno asignado.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, enfermero_asignado: object, antiguedad: int):
        '''
        Inicializa una instancia de `Auxiliar`. Valida el ID, ajusta el salario y asigna los atributos.

        Parámetros
        ----------
        id : str
            Identificador único del auxiliar. Debe comenzar con 'AUX'.
        nombre : str
            Nombre del auxiliar.
        apellido : str
            Apellido del auxiliar.
        edad : int
            Edad del auxiliar.
        genero : str
            Género del auxiliar.
        turno : str
            Turno de trabajo asignado (mañana, tarde, noche).
        horas : int
            Número de horas trabajadas semanalmente.
        salario : float
            Salario base del auxiliar.
        enfermero_asignado : object or None
            Instancia de un enfermero asignado al auxiliar.
        antiguedad : int
            Antigüedad en años del auxiliar.

        Excepciones
        ------
        ValueError
            Si el ID no empieza por 'AUX'.
        '''
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario, str, str)
        self.enfermero_asignado = enfermero_asignado
        self.antiguedad = antiguedad
        if not id.startswith('AUX'):
            raise ValueError('ID inválido, el ID debe empezar por AUX')
        self.salario = self.calculo_salario()

    def calculo_salario(self) -> float:
        '''
        Calcula el salario del auxiliar en función de su antigüedad y turno de trabajo.

        Devuelve
        -------
        float
            El salario ajustado del auxiliar.
        '''
        nuevo_salario = self.salario
        if self.antiguedad <= 2:
            nuevo_salario = self.salario
        elif self.antiguedad > 2 and self.antiguedad <= 7:
            nuevo_salario = 0.10 * self.salario + self.salario
        elif self.antiguedad > 7 and self.antiguedad <= 12:
            nuevo_salario = 0.15 * self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario * 0.25 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.10 + nuevo_salario
        return nuevo_salario  # Devuelve el salario ajustado

    def limpiar_habitacion(self, habitaciones: list) -> list:
        '''
        Limpia las habitaciones que no están limpias y devuelve una lista de las habitaciones que han sido limpiadas.

        Parámetros
        ----------
        habitaciones : list
            Lista de objetos `Habitacion` que el auxiliar debe limpiar.

        Devuelve
        -------
        list
            Lista de habitaciones que fueron limpiadas.
        '''
        habitaciones_limpiadas = []
        for habitacion in habitaciones:
            if not habitacion.limpia:
                habitacion.limpia = True
                print(f'La habitación {habitacion.numero} ha sido limpiada, nuevo estado de la habitación:')
                habitaciones_limpiadas.append(habitacion)
            else:
                print(f'La habitación {habitacion.numero} ya está limpia')
        return habitaciones_limpiadas  # Devuelve la lista de habitaciones limpiadas

    def asignar_enfermero(self, enfermero: object) -> None:
        '''
        Asigna un enfermero al auxiliar, siempre que el auxiliar no tenga un enfermero asignado
        y el enfermero no esté asignado a otro auxiliar.

        Parámetros
        ----------
        enfermero : object
            Instancia de un enfermero a asignar al auxiliar.

        Excepciones
        ----------
        ValueError
            Si el auxiliar ya tiene un enfermero asignado o si el enfermero ya está asignado a otro auxiliar.
        '''
        if self.enfermero_asignado is not None:
            print(f'Error, este auxiliar ya tiene un enfermero asignado: {self.enfermero_asignado.nombre}')
            return
        if enfermero.auxiliar_asignado is not None:
            print(f'El enfermero {enfermero.nombre} ya está asignado')
            return
        self.enfermero_asignado = enfermero
        enfermero.auxiliar_asignado = self
        print(f'El enfermero {enfermero.nombre} se ha asignado correctamente al auxiliar {self.nombre}')


# Ejemplos de objetos `Auxiliar`
auxiliar1 = Auxiliar(
    id='AUX001',
    nombre='Claudia',
    apellido='Mora',
    edad=28,
    genero='Femenino',
    turno='Mañana',
    horas=35,
    salario=1200,
    enfermero_asignado=None,
    antiguedad=1
)

auxiliar2 = Auxiliar(
    id='AUX002',
    nombre='Carlos',
    apellido='Ramírez',
    edad=40,
    genero='Masculino',
    turno='Tarde',
    horas=40,
    salario=1300,
    enfermero_asignado=enfermero1,
    antiguedad=5
)

auxiliar3 = Auxiliar(
    id='AUX003',
    nombre='Lucía',
    apellido='Delgado',
    edad=33,
    genero='Femenino',
    turno='Noche',
    horas=38,
    salario=1250,
    enfermero_asignado=enfermero5,
    antiguedad=10
)

auxiliar4 = Auxiliar(
    id='AUX004',
    nombre='Javier',
    apellido='Gómez',
    edad=45,
    genero='Masculino',
    turno='Noche',
    horas=36,
    salario=1350,
    enfermero_asignado=None,
    antiguedad=13
)

auxiliar5 = Auxiliar(
    id='AUX005',
    nombre='Marina',
    apellido='López',
    edad=29,
    genero='Femenino',
    turno='Mañana',
    horas=30,
    salario=1100,
    enfermero_asignado=None,
    antiguedad=0
)

# Asignación de enfermero
print(auxiliar2.enfermero_asignado)
auxiliar2.asignar_enfermero(enfermero3)
