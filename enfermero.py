# Importación de clases necesarias
from trabajador import Trabajador
from paciente import paciente1, paciente2, paciente4  # Importación de pacientes para asignar a los enfermeros

# Definición de la clase Enfermero que hereda de la clase Trabajador
class Enfermero(Trabajador):
    '''
    Clase que representa a un enfermero, quien hereda de la clase Trabajador.
    Esta clase gestiona la asignación de pacientes, el cálculo de salario en función de la antigüedad y turno,
    y proporciona un método para mostrar la lista de pacientes asignados.

    Atributos
    ----------
    id : str
        Identificador del enfermero (debe empezar por 'ENF').
    nombre : str
        Nombre del enfermero.
    apellido : str
        Apellido del enfermero.
    edad : int
        Edad del enfermero.
    genero : str
        Género del enfermero.
    turno : str
        El turno en el que trabaja el enfermero (mañana, tarde, noche).
    horas : int
        Número de horas trabajadas.
    salario : float
        Salario base.
    especialidad : str
        Especialidad médica del enfermero.
    antiguedad : int
        Años de experiencia del enfermero.
    pacientes_asignados : list
        Lista de pacientes asignados al enfermero.

    Métodos
    -------
    __init__(id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, especialidad: str, antiguedad: int)
        Inicializa los atributos del enfermero y calcula su salario.
    asignar_paciente(paciente: Paciente)
        Asigna un paciente al enfermero.
    calculo_salario() -> float
        Calcula el salario final del enfermero considerando antigüedad y turno.
    mostrar_pacientes() -> str
        Muestra los pacientes asignados al enfermero.
    __str__() -> str
        Devuelve una cadena de texto con la información del enfermero.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, especialidad: str, antiguedad: int):
        '''
        Inicializa los atributos básicos del enfermero, incluyendo especialidad, antigüedad y salario calculado
        en función de la antigüedad y el turno de trabajo.

        Parámetros
        ----------
        id : str
            Identificador del enfermero (debe comenzar con 'ENF').
        nombre : str
            Nombre del enfermero.
        apellido : str
            Apellido del enfermero.
        edad : int
            Edad del enfermero.
        genero : str
            Género del enfermero.
        turno : str
            Turno en el que trabaja el enfermero (mañana, tarde, noche).
        horas : int
            Número de horas trabajadas por el enfermero.
        salario : float
            Salario base del enfermero.
        especialidad : str
            Especialidad médica del enfermero.
        antiguedad : int
            Antigüedad del enfermero (años de experiencia).

        Excepciones
        ------------
        ValueError
            Si el ID no empieza con 'ENF'.
        '''
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.auxiliar_asignado = None
        if not id.startswith('ENF'):
            raise ValueError('ID inválido, el ID debe empezar por ENF')
        self.salario = self.calculo_salario()
        self.pacientes_asignados = []

    def asignar_paciente(self, paciente):
        '''
        Asigna un paciente al enfermero. Si el paciente ya tiene un enfermero asignado, se lanza una excepción.

        Parámetros
        ----------
        paciente : Paciente
            Objeto paciente a asignar al enfermero.

        Excepciones
        ------------
        ValueError
            Si el paciente ya tiene un enfermero asignado.
        '''
        if paciente.enfermero_asignado is not None:
            raise ValueError(f'El paciente {paciente.nombre} ya tiene un enfermero asignado.')
        self.pacientes_asignados.append(paciente)  # Asigna el paciente al enfermero
        paciente.asignar_enfermero(self)  # Asigna este enfermero al paciente

    def calculo_salario(self) -> float:
        '''
        Calcula el salario final del enfermero considerando su antigüedad y turno de trabajo.

        El cálculo del salario varía dependiendo de la antigüedad y si trabaja en el turno de noche.
        La antigüedad también tiene un impacto significativo en el salario.

        Devuelve
        -------
        float
            El salario calculado para el enfermero.
        '''
        nuevo_salario = self.salario
        if self.antiguedad <= 2:
            nuevo_salario = self.salario
        elif self.antiguedad > 2 and self.antiguedad <= 7:
            nuevo_salario = 0.15 * self.salario + self.salario
        elif self.antiguedad > 7 and self.antiguedad <= 12:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario * 0.3 + self.salario
        if self.turno.lower() == 'noche':  # Incremento si el turno es de noche
            nuevo_salario = nuevo_salario * 0.15 + nuevo_salario
        return nuevo_salario

    def mostrar_pacientes(self) -> str:
        '''
        Muestra los pacientes asignados al enfermero.

        Si no hay pacientes asignados, muestra un mensaje indicando que no hay pacientes asignados.

        Devuelve
        -------
        str
            Un string con los detalles de los pacientes asignados.
        '''
        if not self.pacientes_asignados:
            return f'No hay pacientes asignados'
        else:
            pacientes_info = f'Pacientes asignados: '
            for paciente in self.pacientes_asignados:
                pacientes_info += f'Nombre: {paciente.nombre} - Apellido: {paciente.apellido} - ID: {paciente.id} '
            return pacientes_info

    def __str__(self) -> str:
        '''
        Devuelve una representación en formato cadena del enfermero, incluyendo sus detalles básicos.

        Devuelve
        -------
        str
            Cadena con la información del enfermero.
        '''
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - '
                f'Turno: {self.turno} - Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antigüedad: {self.antiguedad}')

# Creación de objetos Enfermero con sus atributos
enfermero1 = Enfermero(
    id="ENF001",
    nombre="Juan",
    apellido="Pérez",
    edad=35,
    genero="Masculino",
    turno="mañana",
    horas=40,
    salario=1800,
    especialidad="UCI",
    antiguedad=6
)

enfermero2 = Enfermero(
    id="ENF002",
    nombre="María",
    apellido="García",
    edad=30,
    genero="Femenino",
    turno="tarde",
    horas=38,
    salario=1750,
    especialidad="Pediatría",
    antiguedad=3
)

enfermero3 = Enfermero(
    id="ENF003",
    nombre="Pedro",
    apellido="López",
    edad=45,
    genero="Masculino",
    turno="noche",
    horas=42,
    salario=1900,
    especialidad="Urgencias",
    antiguedad=10
)

enfermero4 = Enfermero(
    id="ENF004",
    nombre="Laura",
    apellido="Martínez",
    edad=29,
    genero="Femenino",
    turno="mañana",
    horas=36,
    salario=1600,
    especialidad="Oncología",
    antiguedad=1
)

enfermero5 = Enfermero(
    id="ENF005",
    nombre="Andrés",
    apellido="Sánchez",
    edad=50,
    genero="Masculino",
    turno="noche",
    horas=40,
    salario=2000,
    especialidad="Reanimación",
    antiguedad=14
)

enfermero1.asignar_paciente(paciente4)
enfermero2.asignar_paciente(paciente2)
enfermero2.asignar_paciente(paciente1)

print(enfermero2.mostrar_pacientes())

