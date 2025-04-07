from abc import ABC, abstractmethod
class Cita(ABC):
    def __init__(self, id_cita, paciente, medico, fecha, hora, estado='pendiente', atendido=False):
        self.id_cita = id_cita
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.atendido = atendido
    @abstractmethod
    def cancelar_cita(self):
        self.estado = 'cancelado'
        self.atendido = False
        return f'El paciente {self.paciente} ha cancelado la cita {self.id_cita}'
    @abstractmethod
    def ser_atendido(self):
        self.atendido = True
        return self.atendido