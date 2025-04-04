from trabajador import Trabajador

class Enfermero (Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, especialidad, antiguedad):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        if not id.startswith('ENF'):
            raise ValueError('ID inválido, el ID debe empezar por ENF')
        self.salario = self.calculo_salario()

    def calculo_salario(self):
        nuevo_salario = self.salario
        if self.antiguedad <=2:
            nuevo_salario = self.salario
        elif self.antiguedad >2 and self.antiguedad <=7:
            nuevo_salario = 0.15*self.salario + self.salario
        elif self.antiguedad >7 and self.antiguedad <=12:
            nuevo_salario = 0.2*self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario*0.3 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario*0.15 + nuevo_salario
        return nuevo_salario

    def __str__(self):
        return(f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - Turno: {self.turno} - '
              f'- Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')
#Se pueden meter mas cosas: asignar auxiliares, asignar pacientes al igual que en el de medico
