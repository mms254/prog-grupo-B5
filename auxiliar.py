from trabajador import Trabajador

class Auxiliar (Trabajador):
    def __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, enfermero_asignado, antiguedad):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario)
        self.enfermero_asignado = enfermero_asignado
        self.antiguedad = antiguedad
        if not id.startswith('AUX'):
            raise ValueError('ID inválido, el ID debe empezar por AUX')
        self.salario = self.calculo_salario()

    def calculo_salario(self):
        nuevo_salario = self.salario
        if self.antiguedad <=2:
            nuevo_salario = self.salario
        elif self.antiguedad >2 and self.antiguedad <=7:
            nuevo_salario = 0.10*self.salario + self.salario
        elif self.antiguedad >7 and self.antiguedad <=12:
            nuevo_salario = 0.15*self.salario + self.salario
        elif self.antiguedad > 12:
            nuevo_salario = self.salario*0.25 + self.salario
        if self.turno.lower() == 'noche':
            nuevo_salario = nuevo_salario*0.10 + nuevo_salario
        return nuevo_salario

    def limpiar_habitacion(self, habitaciones):
        habitaciones_limpiadas = []
        for habitacion in habitaciones:
            if not habitacion.limpia:
                habitacion.limpia = True
                print(f'La habitacion {habitacion.numero}a sido limpia, nuevo estado de la limpieza de la habitacion:')
                habitaciones_limpiadas.append(habitacion)
            else:
                print(f'La habitacion {habitacion.numero} ya está limpia')
        return habitaciones_limpiadas

    def asignar_enfermero(self, enfermero):
        if self.enfermero_asignado is not None:
            print(f'Error, este auxiliar ya tiene un enfermero asignado: {self.enfermero_asignado.nombre}')
            return
        if enfermero.auxiliar_asignado is not None:
            print(f'El enfermero {enfermero.nombre} ya está asignado')
            return
        self.enfermero_asignado = enfermero
        enfermero.auxiliar_asignado = self
        print(f'El enfermero {enfermero.nombre} se ha asignado correctamente al auxiliar {self.nombre}')