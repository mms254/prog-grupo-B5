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
        if centro in self.centros:
            return f'No puedes añadir este centro porque ya está registrado'
        else:
            self.centros.append(centro)
        return (f'Se ha añadirdo el centro {centro.nombre_centro} correctamente a la provincia {self.nombre_provincia}')
    def eliminar_centro(self, centro):
        if centro not in self.centros:
            return f'No puedes eliminar el centro {centro.nombre_centro} porque este no está registrado'
        else:
            self.centros.remove(centro)
            return (f'Se ha eliminado el centro {centro.nombre_centro} correctamente a la provincia {self.nombre_provincia}')

    def buscar_centro(self, nombre_centro):
        for centro in self.centros:
            if centro.nombre_centro == nombre_centro:
                return centro
        return f'Centro {nombre_centro} no encontrado en la provincia {self.nombre_provincia}'