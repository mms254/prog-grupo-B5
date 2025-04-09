from abc import ABC, abstractmethod


class Cita(ABC):
    '''
    Clase abstracta que representa una cita médica. Los atributos de esta clase incluyen el ID de la cita,
    el paciente, el médico, la fecha y la hora de la cita, el estado (pendiente, cancelado, completado)
    y si la cita ha sido atendida o no. Esta clase es una plantilla para crear objetos de citas médicas
    y debe ser heredada para ser utilizada.

    Atributos
    ---------
    id_cita : str
        Identificador único de la cita.
    paciente : str
        Nombre del paciente.
    medico : str
        Nombre del médico asignado.
    fecha : str
        Fecha en la que se llevará a cabo la cita.
    hora : str
        Hora en la que se llevará a cabo la cita.
    estado : str, opcional
        Estado de la cita. Por defecto es 'pendiente'.
    atendido : bool, opcional
        Si la cita ha sido atendida o no. Por defecto es False.

    Métodos
    --------
    __init__(self, id_cita, paciente, medico, fecha, hora, estado='pendiente', atendido=False)
        Inicializa una nueva cita médica con el ID, paciente, médico, fecha, hora, estado y si ha sido atendida o no.

    cancelar_cita(self)
        Cancela la cita, cambia el estado a 'cancelado' y marca la cita como no atendida.

    ser_atendido(self)
        Marca la cita como atendida y cambia su estado a 'completado'.
    '''

    # Método de inicialización
    def __init__(self, id_cita: str, paciente: str, medico: str, fecha: str, hora: str, estado: str='pendiente', atendido: bool=False):
        '''
        Inicializa una nueva cita médica con el ID, paciente, médico, fecha, hora, estado y si ha sido atendida o no.

        Parámetros
        ----------
        id_cita : str
            Identificador único de la cita.
        paciente : str
            Nombre del paciente.
        medico : str
            Nombre del médico asignado.
        fecha : str
            Fecha en la que se llevará a cabo la cita.
        hora : str
            Hora en la que se llevará a cabo la cita.
        estado : str, opcional
            Estado de la cita, por defecto 'pendiente'.
        atendido : bool, opcional
            Si la cita ha sido atendida o no, por defecto False.
        '''
        # Asignación de los atributos proporcionados
        self.id_cita = id_cita
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.atendido = atendido

    @abstractmethod
    def cancelar_cita(self) -> str:
        '''
        Cancela la cita médica, cambia el estado a 'cancelado' y marca la cita como no atendida.

        Devuelve
        -------
        str
            Mensaje indicando que la cita ha sido cancelada.
        '''
        # Implementación de la cancelación de la cita
        self.estado = 'cancelado'
        self.atendido = False
        return f'El paciente {self.paciente} ha cancelado la cita {self.id_cita}'

    @abstractmethod
    def ser_atendido(self)-> bool:
        '''
        Marca la cita como atendida, cambia el estado a 'completado'.

        Devuelve
        -------
        bool
            Devuelve True para indicar que la cita ha sido atendida.
        '''
        # Cambiar el estado de la cita y marcarla como atendida
        self.atendido = True
        self.estado = 'completado'
        return self.atendido

#Como cita es una clase abstracta, no se pueden crear objetos