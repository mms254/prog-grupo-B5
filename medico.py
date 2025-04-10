from trabajador import Trabajador
from paciente import paciente10, paciente6, paciente1

class Medico(Trabajador):
    '''
    Representa a un médico del sistema sanitario.

    Hereda de
    ---------
    Trabajador

    Atributos
    ---------
    username : str
        Nombre de usuario para el acceso del médico.
    password : str
        Contraseña asociada al usuario.
    especialidad : str
        Área médica en la que está especializado el médico.
    antiguedad : int
        Años de experiencia del médico.
    pacientes_asignados : list
        Lista de objetos de tipo Paciente asignados a este médico.
    salario : float
        Salario ajustado en base a antigüedad y turno.
    '''

    def __init__(self, id: str, username: str, password: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float,especialidad: str,antiguedad: int):
        '''
        Inicializa un objeto Medico con los datos proporcionados y ajusta el salario según la experiencia.

        Parámetros
        ----------
        id : str
            Identificador único del médico, debe comenzar por 'MED'.
        username : str
            Nombre de usuario para el acceso del médico.
        password : str
            Contraseña de acceso.
        nombre : str
            Nombre del médico.
        apellido : str
            Apellido del médico.
        edad : int
            Edad del médico.
        genero : str
            Género del médico.
        turno : str
            Turno de trabajo ('mañana', 'tarde', 'noche').
        horas : int
            Número de horas trabajadas semanalmente.
        salario : float
            Salario base del médico.
        especialidad : str
            Especialidad médica del profesional.
        antiguedad : int
            Años de experiencia laboral en el sector.

        Excepciones
        -----------
        ValueError
            Si el ID no comienza por 'MED'.
        '''
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.username = username
        self.password = password
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.pacientes_asignados = []
        self.salario = self.calculo_salario()
        if not id.startswith('MED'):
            raise ValueError('ID inválido, el ID debe empezar por MED')

    def calculo_salario(self) -> float:
        '''
        Calcula el salario ajustado del médico en base a su antigüedad y turno.

        Devuelve
        --------
        float
            Salario ajustado del médico.
        '''
        nuevo_salario = self.salario
        if self.antiguedad <= 1:
            nuevo_salario = self.salario
        elif self.antiguedad <= 5:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad <= 10:
            nuevo_salario = 0.3 * self.salario + self.salario
        else:
            nuevo_salario = 0.5 * self.salario + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.2 + nuevo_salario
        return nuevo_salario

    def asignar_paciente(self, paciente: object) -> None:
        '''
        Asigna un paciente al médico si no está ya asignado.

        Parámetros
        ----------
        paciente : object
            Objeto de tipo Paciente a asignar.
        '''
        if paciente in self.pacientes_asignados:
            print(f'El paciente {paciente.nombre} ya está asignado a este médico.')
        else:
            self.pacientes_asignados.append(paciente)
            print(f'Paciente {paciente.nombre} asignado al médico {self.nombre}.')

    def obtener_historial_pacientes(self, paciente: object) -> list:
        '''
        Obtiene la lista de pacientes asignados al médico.

        Parámetros
        ----------
        paciente : object
            Objeto de tipo Paciente.

        Devuelve
        --------
        list
            Lista de pacientes asignados al médico.
        '''
        historial_pacientes = []
        if not self.pacientes_asignados:
            return f'No hay pacientes asignados actualmente.'
        else:
            for paciente in self.pacientes_asignados:
                historial_pacientes.append(paciente)
            return historial_pacientes

    def to_dict(self) -> dict:
        '''
        Convierte la información del médico en un diccionario.

        Devuelve
        --------
        dict
            Diccionario con los atributos clave del médico.
        '''
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'genero': self.genero,
            'horas': self.horas,
            'especialidad': self.especialidad,
            'antiguedad': self.antiguedad,
            'turno': self.turno.lower(),
            'rol': self.rol,
            'pacientes_asignados': self.pacientes_asignados,
            'salario': self.salario
        }

    def __str__(self) -> str:
        '''
        Devuelve una representación en texto del objeto médico.

        Devuelve
        --------
        str
            Representación en texto del médico.
        '''
        return (
            f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - Turno: {self.turno} - '
            f'Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}'
        )

# Creación de objetos Medico con sus atributos
medico1 = Medico(
    id='MED001',
    username='juanmed',
    password='1234',
    nombre='Juan',
    apellido='Pérez',
    edad=45,
    genero='Masculino',
    turno='Día',
    horas=40,
    salario=3000.00,
    especialidad='Cardiología',
    antiguedad=12
)

medico2 = Medico(
    id='MED002',
    username='anamed',
    password='abcd',
    nombre='Ana',
    apellido='Gómez',
    edad=38,
    genero='Femenino',
    turno='Noche',
    horas=36,
    salario=2800.00,
    especialidad='Pediatría',
    antiguedad=6
)

medico3 = Medico(
    id='MED003',
    username='carlosneu',
    password='neu123',
    nombre='Carlos',
    apellido='Martínez',
    edad=50,
    genero='Masculino',
    turno='Día',
    horas=42,
    salario=3500.00,
    especialidad='Neurología',
    antiguedad=15
)

medico4 = Medico(
    id='MED004',
    username='marialop',
    password='mlop456',
    nombre='María',
    apellido='Lopez',
    edad=40,
    genero='Femenino',
    turno='Día',
    horas=38,
    salario=3100.00,
    especialidad='Traumatología',
    antiguedad=8
)

medico5 = Medico(
    id='MED005',
    username='luissan',
    password='ls123',
    nombre='Luis',
    apellido='Sánchez',
    edad=35,
    genero='Masculino',
    turno='Noche',
    horas=40,
    salario=2900.00,
    especialidad='Dermatología',
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

print(medico1.obtener_historial_pacientes(paciente10))
