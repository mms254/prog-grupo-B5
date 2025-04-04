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
        for habitacion in habitaciones:
            if not habitacion.limpia:
                habitacion.limpia = True
                print(f'La habitacion {habitacion.numero}a sido limpia, nuevo estado de la limpieza de la habitacion:')
                return habitacion.limpia
            else:
                print(f'La habitacion {habitacion.numero} ya está limpia')
# Añadir asignar enfermero
