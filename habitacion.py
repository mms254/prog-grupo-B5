from centro import Centro

class Habitacion(Centro):
    def __init__(self, nombre_comunidad, nombre_provincia, id_centro, nombre_centro, cantidad_trabajadores, presupuesto,
                 habitaciones, numero_habitacion, capacidad, limpia=False):
        super().__init__(nombre_comunidad, nombre_provincia, id_centro, nombre_centro, cantidad_trabajadores,
                         presupuesto)
        self.numero_habitacion = numero_habitacion
        self.capacidad = capacidad
        self.limpia = limpia
        self.pacientes = []
        self.habitaciones = habitaciones

    def obtener_info(self):
        info = f'Habitacion: {self.numero_habitacion} - Limpia: {self.limpia} - Capacidad: {self.capacidad} - Pacientes asignados: {self.pacientes} - Cantidad de pacientes: {len(self.pacientes)}'
        return info

    def limpiar(self):
        if self.limpia == False:
            self.limpia = True
            print(f'La habitación {self.numero_habitacion} ha sido limpiada.')
        else:
            print(f'La habitación {self.numero_habitacion} ya está limpia.')
# Añadir metodo de asignar pacientes a la habitacion con append
