from persona import Persona

class Trabajador(Persona):
    '''
    Clase que representa a un trabajador del sistema hospitalario, heredando de Persona.
    Contiene información sobre su turno, horas diarias y salario mensual.

    Atributos
    ----------
    id : str
        Identificador único del trabajador.
    nombre : str
        Nombre del trabajador.
    apellido : str
        Apellido del trabajador.
    edad : int
        Edad del trabajador.
    genero : str
        Género del trabajador.
    turno : str
        Turno en el que trabaja (mañana, tarde, noche).
    horas : int
        Número de horas que trabaja al día.
    salario : float
        Salario mensual del trabajador.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int, salario: float = 0.0) -> None:
        '''
        Inicializa los atributos del trabajador.

        Parámetros
        ----------
        id : str
            Identificador único del trabajador.
        nombre : str
            Nombre del trabajador.
        apellido : str
            Apellido del trabajador.
        edad : int
            Edad del trabajador.
        genero : str
            Género del trabajador.
        turno : str
            Turno de trabajo (mañana, tarde, noche).
        horas : int
            Número de horas que trabaja al día.
        salario : float, opcional
            Salario mensual del trabajador. Por defecto es 0.0.
        '''
        super().__init__(id, nombre, apellido, edad, genero)
        self.turno = turno
        self.horas = horas
        self.salario = salario

    def calcular_horas_trabajadas_mes(self, dias_trabajados: int) -> None:
        '''
        Calcula el total de horas trabajadas por el trabajador en un mes.

        Parámetros
        ----------
        dias_trabajados : int
            Número de días trabajados en el mes.

        Devuelve
        -------
        None
            Imprime el total de horas trabajadas en el mes.
        '''
        horas_trabajadas = self.horas * dias_trabajados
        print(f'El trabajador {self.nombre} ha trabajado un total de {horas_trabajadas} horas este mes.')

    def cambiar_turno(self, nuevo_turno: str) -> None:
        '''
        Cambia el turno actual del trabajador.

        Parámetros
        ----------
        nuevo_turno : str
            Nuevo turno que se asignará al trabajador.

        Devuelve
        -------
        None
            Imprime un mensaje confirmando el cambio de turno.
        '''
        self.turno = nuevo_turno
        print(f'El turno del médico {self.nombre}, con ID: {self.id} ha sido cambiado a {self.turno}.')

    def horas_extras(self, horas_extra: int) -> None:
        '''
        Calcula la paga extra por horas adicionales y actualiza el salario del trabajador.

        Parámetros
        ----------
        horas_extra : int
            Número de horas extras trabajadas.

        Devuelve
        -------
        None
            Actualiza el salario del trabajador con la paga correspondiente por horas extra.
        '''
        paga_extra = horas_extra * (self.salario / self.horas)
        self.salario += paga_extra

    def despedir(self) -> str:
        '''
        Marca al trabajador como despedido.

        Devuelve
        -------
        str
            Mensaje indicando que el trabajador ha sido despedido.
        '''
        self.trabajar = False
        return f'El trabajador {self.nombre} con id {self.id} ha sido despedido'
trabajador1 = Trabajador(id='T001', nombre='Ana', apellido='Gómez', edad=34, genero='Femenino', turno='mañana', horas=8, salario=1800.0)
trabajador2 = Trabajador(id='T002', nombre='Luis', apellido='Martínez', edad=42, genero='Masculino', turno='tarde', horas=7, salario=1650.0)
trabajador3 = Trabajador(id='T003', nombre='Claudia', apellido='Ruiz', edad=29, genero='Femenino', turno='noche', horas=10, salario=2000.0)
trabajador4 = Trabajador(id='T004', nombre='Andrés', apellido='Pérez', edad=50, genero='Masculino', turno='mañana', horas=6, salario=1500.0)
trabajador5 = Trabajador(id='T005', nombre='Sara', apellido='Navarro', edad=38, genero='Femenino', turno='tarde', horas=8, salario=1700.0)

trabajador1.horas_extras(10)
print(trabajador2.despedir())
trabajador5.cambiar_turno('Noche')
trabajador3.calcular_horas_trabajadas_mes(20)