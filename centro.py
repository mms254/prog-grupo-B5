from provincia import Provincia
class Centro(Provincia):
    ids_usados = set()
    def __init__(self, nombre_comunidad, nombre_provincia, id_centro, nombre_centro, cantidad_trabajadores, presupuesto,
                 habitaciones):
        super().__init__(nombre_comunidad, nombre_provincia)
        self.id_centro = id_centro
        self.nombre_centro = nombre_centro
        self.cantidad_trabajadores = cantidad_trabajadores
        self.presupuesto = presupuesto
        self.habitaciones = habitaciones
        if id_centro in Centro.ids_usados:
            raise ValueError(f'El ID: {id_centro} ya está en uso.')
        Centro.ids_usados.add(id_centro)
        if presupuesto <0:
            raise ValueError('No se admiten presupuestos negativos')
        if cantidad_trabajadores<0:
            raise ValueError('NO se adimiten cantidades negativas de trabajadores')
        if habitaciones<0:
            raise ValueError('No se adimiten habitaciones negativas')
    def añadir_trabajadores(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError('No se admiten cantidades negativas de trabajadores')
        else:
            self.cantidad_trabajadores += nueva_cantidad
    def añadir_habitaciones(self, cantidad_habitaciones):
        if cantidad_habitaciones<0:
            raise ValueError('No admiten cantidades negativas de habitaciones')
        else:
            self.habitaciones +=cantidad_habitaciones
    def pagos(self, pago):
        if self.presupuesto + pago <0:
            raise ValueError('No se admiten presupuestos negativos')
        else:
            self.presupuesto += pago
    def obtener_info(self):
        info = f'Centro médico: {self.nombre_centro}\n'
        info += f'ID Centro: {self.id_centro}\n'
        info += f'Cantidad de trabajadores: {self.cantidad_trabajadores}\n'
        info += f'Habitaciones disponibles: {self.habitaciones}\n'
        info += f'Presupuesto: {self.presupuesto}€\n'
        return info