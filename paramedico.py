from trabajador import Trabajador
class Paramedico(Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, especialidad, antiguedad):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.ambulancia_asignada = None

    def asignar_ambulancia(self, ambulancia):
        if self.ambulancia_asignada is not None:
            raise ValueError(f'El paramédico {self.nombre} ya está asignado a una ambulancia.')
        self.ambulancia_asignada = ambulancia
        ambulancia.asignar_paramedico(self)

    def __str__(self):
        if self.ambulancia_asignada is not None:
            return (f'Nombre: {self.nombre} - ID: {self.id} - Edad: {self.edad} - Género: {self.genero} - Turno: {self.turno} - Horas: {self.horas} - '
                    f' Salario: {self.salario} - Especialidad: {self.especialidad} - Antiguedad: {self.antiguedad} - Ambulancia: {self.ambulancia_asignada.matricula}')
