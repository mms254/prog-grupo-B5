from persona import Persona

class Trabajador (Persona):
    def __init__(self, id, nombre, apellido, edad, genero, turno,contratacion, horas, salario=0):
        super().__init__(id, nombre, apellido, edad, genero)
        self.turno = turno
        self.contratacion = contratacion
        self.horas = horas
        self.salario = salario

    def calcular_horas_trabajadas_mes(self, dias_trabajados):
        horas_trabajadas = self.horas * dias_trabajados
        print(f'El trabajador {self.nombre} ha trabajado un total de {horas_trabajadas} horas este mes.')

    def cambiar_turno(self, nuevo_turno):
        self.turno = nuevo_turno
        print(f'El turno del médico {self.nombre}, con ID: {self.id} ha sido cambiado a {self.turno}.')

    def horas_extras(self, horas_extra):
        paga_extra = horas_extra  * (self.salario / self.horas)
        self.salario += paga_extra

    def despedir(self):
        self.trabajar = False
        return f'El trabajador {self.nombre} con id {self.id} ha sido despedido'