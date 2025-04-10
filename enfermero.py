# enfermero.py
from trabajador import Trabajador

class Enfermero(Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, especialidad, antiguedad, password):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.especialidad = especialidad
        self.antiguedad = antiguedad
        self.auxiliar_asignado = None
        self.pacientes_asignados = []
        self.password = password
        self.rol = "enfermero"

        if not id.startswith('ENF'):
            raise ValueError('ID inválido, el ID debe empezar por ENF')

        self.salario = self.calculo_salario()

    def calculo_salario(self):
        nuevo_salario = self.salario
        if self.antiguedad <= 2:
            nuevo_salario = self.salario
        elif 2 < self.antiguedad <= 7:
            nuevo_salario = 0.15 * self.salario + self.salario
        elif 7 < self.antiguedad <= 12:
            nuevo_salario = 0.2 * self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario * 0.3 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario * 0.15 + nuevo_salario
        return nuevo_salario

    def asignar_auxiliar(self, auxiliar):
        self.auxiliar_asignado = auxiliar

    def asignar_paciente(self, paciente):
        if paciente.enfermero_asignado is not None:
            raise ValueError(f'El paciente {paciente.nombre} ya tiene un enfermero asignado.')
        self.pacientes_asignados.append(paciente)
        paciente.asignar_enfermero(self)

    def mostrar_pacientes(self):
        if not self.pacientes_asignados:
            return 'No hay pacientes asignados'
        else:
            pacientes_info = 'Pacientes asignados: '
            for paciente in self.pacientes_asignados:
                pacientes_info += f'Nombre: {paciente.nombre} - Apellido: {paciente.apellido} - ID: {paciente.id}, '
            return pacientes_info.rstrip(', ')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "genero": self.genero,
            "turno": self.turno,
            "horas": self.horas,
            "salario": self.salario,
            "especialidad": self.especialidad,
            "antiguedad": self.antiguedad,
            "password": self.password,
            "rol": self.rol,
            "pacientes_asignados": [paciente.id for paciente in self.pacientes_asignados]
        }

    def __str__(self):
        return (f'ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Género: {self.genero} - Turno: {self.turno} '
                f'- Horas: {self.horas} - Especialidad: {self.especialidad} - Salario: {self.salario} - Antiguedad: {self.antiguedad}')
