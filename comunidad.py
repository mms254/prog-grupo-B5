from abc import ABC, abstractmethod

class Comunidad(ABC):
    def __init__(self, nombre_comunidad):
        self.nombre_comunidad = nombre_comunidad
        self.presupuesto

    def obtener_info(self):
        pass

    def asignar_presupuesto(self, cantidad):
        self.presupuesto +=cantidad