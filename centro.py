from provincia import Provincia

class Centro(Provincia):
    def __init__(self, nombre_comunidad, nombre_provincia, id_centro, nombre_centro, cantidad_trabajadores, presupuesto,
                 habitaciones):
        super().__init__(nombre_comunidad, nombre_provincia)
        self.id_centro = id_centro
        self.nombre_centro = nombre_centro
        self.cantidad_trabajadores = cantidad_trabajadores
        self.presupuesto = presupuesto
        self.habitaciones = habitaciones

    def obtener_info(self):
        info = f'Centro médico: {self.nombre_centro}\n'
        info += f'ID Centro: {self.id_centro}\n'
        info += f'Cantidad de trabajadores: {self.cantidad_trabajadores}\n'
        info += f'Habitaciones disponibles: {self.habitaciones}\n'
        info += f'Presupuesto: {self.presupuesto}€\n'
        return info
