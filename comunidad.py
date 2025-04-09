from abc import ABC, abstractmethod

class Comunidad(ABC):
    def __init__(self, nombre_comunidad):
        self.nombre_comunidad = nombre_comunidad
        self.presupuesto = 0
    def obtener_info(self):
        return f'Nombre: {self.nombre_comunidad} - Presupuesto: {self.presupuesto}'
    def asignar_presupuesto(self, cantidad):
        if cantidad < 0:
            raise ValueError('No se admiten presupuestos negativos')
        else:
            self.presupuesto +=cantidad
            return f'Nuevo presupuesto para {self.nombre_comunidad}: {self.presupuesto}€'
    @abstractmethod
    def gestionar_centros(self):
        pass
