class Documento:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.urgente = False
        self.prioridad = 0

    def validar_documento(self):
        if not self.titulo or not self.descripcion:
            raise ValueError('El documento no es valido, ingrese un documento con contenido de titulo y descripcion')
        else:
            return True

    def marcar_urgente (self):
        self.urgente = True
        self.prioridad = 1
        return (f'El documento {self.titulo} es urgente')

    def prioritarios (self):
        if self.urgente:
            self.prioridad = 1
        else:
            self.proridad = 0
