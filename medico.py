from trabajador import Trabajador

class Medico(Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, contratacion, horas, salario, especialidad,
                 antiguedad):
        super().__init__(id, nombre, apellido, edad, genero, turno, contratacion, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.salario = self.calculo_salario()
        self.disponibilidad = True
        if not id.startswith('MED'):
            raise ValueError('ID inválido, el ID debe empezar por MED')

    def calculo_salario(self):
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

    def __str__(self):
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - Turno: {self.turno} - '
                f'Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')
        # Se puede añadir: asignar pacientes (no lo añado porque no se si piso a algun compañero), verificar la disponibilidad del medico