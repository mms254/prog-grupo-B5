from abc import ABC, abstractmethod
from datetime import datetime

class Cita(ABC):
    def __init__(self, id_cita, paciente, medico, fecha_hora: str, motivo: str, estado='pendiente', atendido=False):
        self.id_cita = id_cita
        self.paciente = paciente
        self.medico = medico
        self.fecha_hora = fecha_hora
        self.motivo = motivo
        self.fecha_hora_dt = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
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
        self.estado = 'completado'
        return self.atendido

    def se_solapa(self, otra_cita) -> bool:
        delta = abs((self.fecha_hora_dt - otra_cita.fecha_hora_dt).total_seconds())
        return delta < 1800

    def to_dict(self):
        return {
            "paciente": self.paciente,
            "medic": self.medico,
            "fecha_hora": self.fecha_hora,
            "motivo": self.motivo
        }
