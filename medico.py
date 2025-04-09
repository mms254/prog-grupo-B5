from trabajador import Trabajador

class Medico(Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, contratacion, horas, salario, especialidad,
                 antiguedad):
        super().__init__(id, nombre, apellido, edad, genero, turno, contratacion, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.pacientes_asignados = []
        self.salario = self.calculo_salario()
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

    def asignar_paciente(self, paciente):
        if paciente in self.pacientes_asignados:
            print(f'El paciente {paciente.nombre} ya está asignado a este médico.')
        else:
            self.pacientes_asignados.append(paciente)
            print(f'Paciente {paciente.nombre} asignado al médico {self.nombre}.')

    def obtener_historial_pacientes(self, paciente):
        historial_pacientes = []
        if not self.pacientes_asignados:
            return f'No hay pacientes asignados actualmente.'
        else:
            for paciente in self.pacientes_asignados:
                historial_pacientes.append(paciente)
            return historial_pacientes

    def __str__(self):
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero} - Turno: {self.turno} - '
                f'Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')