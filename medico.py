from trabajador import Trabajador
from paciente import paciente1, paciente10, paciente6
class Medico(Trabajador):
    '''
    Clase que representa a un médico, que hereda de la clase `Trabajador`, y que incluye atributos y métodos específicos
    para gestionar pacientes asignados y calcular el salario en función de la antigüedad y turno.

    Atributos
    ---------
    id : str
        Identificador único del médico. Debe comenzar con "MED".
    nombre : str
        Nombre del médico.
    apellido : str
        Apellido del médico.
    edad : int
        Edad del médico.
    genero : str
        Género del médico.
    turno : str
        El turno en el que trabaja el médico (ej. "día" o "noche").
    horas : int
        Número de horas trabajadas por el médico.
    salario : float
        Salario base del médico.
    especialidad : str
        Especialidad del médico.
    disponibilidad : bool
        Disponibilidad del medico
    antiguedad : int
        Años de experiencia del médico.
    pacientes_asignados : list
        Lista de pacientes asignados al médico.

    Métodos
    -------
    __init__(id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, especialidad: str, antiguedad: int)
        Inicializa los atributos del médico, con validación del ID y cálculo del salario.
    calculo_salario() -> float
        Calcula el salario del médico en función de la antigüedad y el turno de trabajo.
    asignar_paciente(paciente: Paciente) -> None
        Asigna un paciente al médico, si no está ya asignado.
    obtener_historial_pacientes() -> list
        Devuelve una lista con los pacientes asignados al médico.
    __str__() -> str
        Devuelve una cadena con la información del médico en formato legible.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float, especialidad: str, antiguedad: int):
        '''
        Inicializa los atributos del médico, con validación del ID y cálculo del salario.

        Parámetros
        ----------
        id : str
            Identificador único del médico. Debe comenzar con "MED".
        nombre : str
            Nombre del médico.
        apellido : str
            Apellido del médico.
        edad : int
            Edad del médico.
        genero : str
            Género del médico.
        turno : str
            Turno de trabajo del médico (ej. "noche" o "día").
        horas : int
            Número de horas trabajadas.
        salario : float
            Salario base del médico.
        disponibilidad : bool
            Disponibilidad del medico.
        especialidad : str
            Especialidad del médico.
        antiguedad : int
            Antigüedad (años de experiencia del médico).

        Excepciones
        ------------
        ValueError
            Si el ID no empieza con "MED".
        '''
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.pacientes_asignados = []
        self.salario = self.calculo_salario()
        self.disponibilidad = True
        if not id.startswith('MED'):
            raise ValueError('ID inválido, el ID debe empezar por MED')

    def calculo_salario(self) -> float:
        '''
        Calcula el salario del médico en función de la antigüedad y el turno de trabajo.

        Devuelve
        -------
        float
            El salario calculado del médico.
        '''
        nuevo_salario = self.salario
        if self.antiguedad <= 1:
            nuevo_salario = self.salario
        elif self.antiguedad > 1 and self.antiguedad <= 5:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad > 5 and self.antiguedad <= 10:
            nuevo_salario = 0.3 * self.salario + self.salario
        elif self.antiguedad > 10:
            nuevo_salario = self.salario * 0.5 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.2 + nuevo_salario
        return nuevo_salario

    def asignar_paciente(self, paciente) -> None:
        '''
        Asigna un paciente al médico, si no está ya asignado.

        Parámetros
        ----------
        paciente : Paciente
            El paciente que se va a asignar al médico.

        Devuelve
        -------
        None
        '''
        if paciente in self.pacientes_asignados:
            print(f'El paciente {paciente.nombre} ya está asignado a este médico.')
        else:
            self.pacientes_asignados.append(paciente)
            print(f'Paciente {paciente.nombre} asignado al médico {self.nombre}.')

    def obtener_historial_pacientes(self) -> list:
        '''
        Devuelve una lista con los pacientes asignados al médico.

        Devuelve
        -------
        list
            Lista de objetos pacientes asignados al médico.
        '''
        historial_pacientes = []
        if not self.pacientes_asignados:
            return f'No hay pacientes asignados actualmente.'
        else:
            for paciente in self.pacientes_asignados:
                historial_pacientes.append(str(paciente))
            return historial_pacientes

    def __str__(self) -> str:
        '''
        Devuelve una cadena con la información del médico en formato legible.

        Devuelve
        -------
        str
            Información del médico.
        '''
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - Turno: {self.turno} - '
                f'Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')
# Creación de objetos Medico con sus atributos
medico1 = Medico(
    id="MED001",
    nombre="Juan",
    apellido="Pérez",
    edad=45,
    genero="Masculino",
    turno="Día",
    horas=40,
    salario=3000.00,
    especialidad="Cardiología",
    antiguedad=12
)

medico2 = Medico(
    id="MED002",
    nombre="Ana",
    apellido="Gómez",
    edad=38,
    genero="Femenino",
    turno="Noche",
    horas=36,
    salario=2800.00,
    especialidad="Pediatría",
    antiguedad=6
)

medico3 = Medico(
    id="MED003",
    nombre="Carlos",
    apellido="Martínez",
    edad=50,
    genero="Masculino",
    turno="Día",
    horas=42,
    salario=3500.00,
    especialidad="Neurología",
    antiguedad=15
)

medico4 = Medico(
    id="MED004",
    nombre="María",
    apellido="Lopez",
    edad=40,
    genero="Femenino",
    turno="Día",
    horas=38,
    salario=3100.00,
    especialidad="Traumatología",
    antiguedad=8
)

medico5 = Medico(
    id="MED005",
    nombre="Luis",
    apellido="Sánchez",
    edad=35,
    genero="Masculino",
    turno="Noche",
    horas=40,
    salario=2900.00,
    especialidad="Dermatología",
    antiguedad=4
)
print(medico1)
print(medico2)
print(medico3)
print(medico4)
print(medico5)

medico1.asignar_paciente(paciente10)
medico1.asignar_paciente(paciente6)
medico5.asignar_paciente(paciente1)
print(medico1.obtener_historial_pacientes())