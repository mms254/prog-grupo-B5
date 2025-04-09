class Habitacion:
    def __init__(self, numero_habitacion, capacidad, limpia=False):
        self.numero_habitacion = numero_habitacion
        self.capacidad = capacidad
        self.limpia = limpia
        self.pacientes = []
        self.historial_pacientes= []

    def obtener_info(self):
        info = f'Habitacion: {self.numero_habitacion} - Limpia: {self.limpia} - Capacidad: {self.capacidad} - Pacientes asignados: {self.pacientes} - Cantidad de pacientes: {len(self.pacientes)}'
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