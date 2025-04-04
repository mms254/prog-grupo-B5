from comunidad import Comunidad

class Provincia(Comunidad):
    def __init__(self, nombre_comunidad, nombre_provincia):
        super().__init__(nombre_comunidad)
        self.nombre_provincia = nombre_provincia
        self.centros = []

    def obtener_info(self):
        info = f'Comunidad: {self.nombre_comunidad}\n'
        info += f'Provincia: {self.nombre_provincia}\n'
        info += f'Centros médicos: {len(self.centros)}\n'
        info += f'Presupuesto: {self.presupuesto}€\n'
        return info

    def añadir_centro(self, centro):
        self.centros.append(centro)
        return (f'Se ha añadirdo el centro {centro.nombre_centro} correctamente a la provincia {self.nombre_provincia}')