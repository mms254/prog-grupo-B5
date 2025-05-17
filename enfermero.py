# enfermero.py
from trabajador import Trabajador
from paciente import Paciente
class Enfermero(Trabajador):
    '''
    Clase que representa a un enfermero del sistema hospitalario. Hereda de la clase Trabajador y añade
    atributos y comportamientos específicos como especialidad, antigüedad, cálculo de salario y gestión de pacientes.


    Parámetros
    ----------
    id : str
        Identificador del enfermero. Debe comenzar por 'ENF'.
    nombre : str
        Nombre del enfermero.
    apellido : str
        Apellido del enfermero.
    edad : int
        Edad del enfermero.
    genero : str
        Género del enfermero.
    turno : str
        Turno de trabajo del enfermero ('mañana', 'tarde' o 'noche').
    horas : int
        Cantidad de horas trabajadas por semana.
    salario : float
        Salario base del enfermero.
    especialidad : str
        Especialidad del enfermero.
    antiguedad : int
        Años de experiencia o servicio.
    username : str
        Nombre de usuario para el sistema.
    password : str
        Contraseña para el sistema.

    Excepciones
    -----------
    ValueError
        Si el ID no comienza con 'ENF'.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str,
                 turno: str, horas: int, salario: float, especialidad: str,
                 antiguedad: int, username: str, password: str):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario, str, str)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.salario = self.calculo_salario()
        self.auxiliar_asignado = None
        self.pacientes_asignados = []
        self.username = username
        self.password = password
        self.rol = 'enfermero'

        if not id.startswith('ENF'):
            raise ValueError('ID inválido, el ID debe empezar por ENF')


    def calculo_salario(self):
        nuevo_salario = self.salario
        if self.antiguedad <= 2:
            nuevo_salario = self.salario
        elif 2 < self.antiguedad <= 7:
            nuevo_salario = 0.15 * self.salario + self.salario
        elif 7 < self.antiguedad <= 12:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario * 0.3 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.15 + nuevo_salario
        return nuevo_salario

def asignar_auxiliar(self, auxiliar):
        self.auxiliar_asignado = auxiliar

def calculo_salario(self) -> float:
        '''
        Calcula el salario final del enfermero en función de la antigüedad y el turno.

        Devuelve
        --------
        float
            Salario actualizado del enfermero.
        '''
        nuevo_salario = self.salario
        if self.antiguedad <= 2:
            nuevo_salario = self.salario
        elif 2 < self.antiguedad <= 7:
            nuevo_salario = 0.15 * self.salario + self.salario
        elif 7 < self.antiguedad <= 12:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario * 0.3 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.15 + nuevo_salario
        return nuevo_salario

def asignar_paciente(self, paciente) -> None:
        '''
        Asigna un paciente al enfermero si aún no tiene uno asignado.

        Parámetros
        ----------
        paciente : Paciente
            Instancia de la clase Paciente que será asignada.

        Excepciones
        -----------
        ValueError
            Si el paciente ya tiene un enfermero asignado.
        '''
        if paciente.enfermero_asignado is not None:
            raise ValueError(f'El paciente {paciente.nombre} ya tiene un enfermero asignado.')
        self.pacientes_asignados.append(paciente)
        paciente.asignar_enfermero(self)


def mostrar_pacientes(self) -> str:
        '''
        Genera una cadena con la información de los pacientes asignados al enfermero.

        Devuelve
        --------
        str
            Lista formateada de pacientes o un mensaje indicando que no hay pacientes asignados.
        '''

def mostrar_pacientes(self):
    if not self.pacientes_asignados:
        return 'No hay pacientes asignados'
    else:
        pacientes_info = 'Pacientes asignados: '
        for paciente in self.pacientes_asignados:
            pacientes_info += f'Nombre: {paciente.nombre} - Apellido: {paciente.apellido} - ID: {paciente.id}, '
        return pacientes_info.rstrip(', ')


def to_dict(self) -> dict:
        '''
        Convierte el objeto Enfermero a un diccionario con sus atributos principales.

        Devuelve
        --------
        dict
            Diccionario representando el estado del objeto.
        '''
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'genero': self.genero,
            'turno': self.turno,
            'horas': self.horas,
            'salario': self.salario,
            'especialidad': self.especialidad,
            'antiguedad': self.antiguedad,
            'username': self.username,
            'password': self.password,
            'rol': self.rol,
            'pacientes_asignados': [paciente.id for paciente in self.pacientes_asignados]
        }

def __str__(self) -> str:
        '''
        Representación en forma de cadena del enfermero.

        Devuelve
        --------
        str
            Cadena con los atributos más relevantes del enfermero.
        '''
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Género: {self.genero} - Turno: {self.turno} '
                f'- Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')



