from paciente import paciente10
from paciente import paciente11
from paciente import paciente5
class Habitacion:
    def __init__(self, numero_habitacion, capacidad, limpia=False):
        self.numero_habitacion = numero_habitacion
        self.capacidad = capacidad
        self.limpia = limpia
        self.pacientes = []
        self.historial_pacientes= []
        self.pacientes_info = []

    def obtener_info(self):
        for paciente in self.pacientes:
            self.pacientes_info.append(str(paciente.nombre))
        info = f'Habitacion: {self.numero_habitacion} - Limpia: {self.limpia} - Capacidad: {self.capacidad} - Pacientes asignados: {self.pacientes_info} - Cantidad de pacientes: {len(self.pacientes)}'
        return info
    def __len__(self):
        return len(self.pacientes)

    def limpiar(self):
        if not self.limpia:
            self.limpia = True
            print(f'La habitación {self.numero_habitacion} ha sido limpiada.')
        else:
            print(f'La habitación {self.numero_habitacion} ya está limpia.')
    def añadir_pacientes(self, paciente):
        if len(self) >= self.capacidad:
            raise ValueError(f'La cantidad de pacientes de la habitacion {self.numero_habitacion} sobrepasa su capacidad: {self.capacidad}')
        if paciente in self.pacientes:
            raise ValueError (f'El paciente {paciente.nombre} ya está registrado en la habitacion {self.numero_habitacion}')
        else:
            self.pacientes.append(paciente)
            self.historial_pacientes.append(paciente)
        return self.pacientes

    def eliminar_paciente(self, paciente):
        if paciente in self.pacientes:
            self.pacientes.remove(paciente)
            print(f'Paciente {paciente.nombre} eliminado de la habitación {self.numero_habitacion}.')
        else:
            print(f'Paciente {paciente.nombre} no está en la habitación {self.numero_habitacion}.')

habitacion1 = Habitacion(99, 4)
habitacion2 = Habitacion(54, 1)
habitacion3 = Habitacion(109, 2)
habitacion4 = Habitacion(90, 3)
habitacion5 = Habitacion(190, 10)

habitacion2.limpiar()
habitacion4.añadir_pacientes(paciente11)
habitacion4.añadir_pacientes(paciente10)
print(habitacion4.obtener_info())
habitacion4.eliminar_paciente(paciente10)
