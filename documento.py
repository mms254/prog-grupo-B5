class Documento:
    '''
    Clase que representa un documento, con título, descripción y un indicador de urgencia y prioridad.

    Atributos
    ----------
    titulo : str
        Título del documento.
    descripcion : str
        Descripción del documento.
    urgente : bool
        Indica si el documento es urgente o no. Inicialmente es False.
    prioridad : int
        Define la prioridad del documento. 0 es normal, 1 es urgente. Inicialmente es 0.

    Métodos
    -------
    marcar_urgente() :
        Marca el documento como urgente, estableciendo su prioridad a 1.
        Devuelve un mensaje indicando que el documento es urgente.

    prioritarios() :
        Devuelve el valor de la prioridad del documento (1 si es urgente, 0 si no lo es).
    '''

    def __init__(self, titulo: str, descripcion: str):
        '''
        Inicializa una instancia de `Documento` con título y descripción.

        Parámetros
        ----------
        titulo : str
            Título del documento.
        descripcion : str
            Descripción del documento.

        Excepciones
        ------------
        ValueError
            Si el título o la descripción están vacíos.
        '''
        self.titulo = titulo
        self.descripcion = descripcion
        self.urgente = False
        self.prioridad = 0
        if not self.titulo or not self.descripcion:
            raise ValueError('El documento no es valido, ingrese un documento con contenido de titulo y descripcion')

    def marcar_urgente(self) -> str:
        '''
        Marca el documento como urgente y establece su prioridad a 1.

        Devuelve
        -------
        str
            Mensaje indicando que el documento es urgente.
        '''
        self.urgente = True
        self.prioridad = 1
        return f'El documento {self.titulo} es urgente'

    def prioritarios(self) -> int:
        '''
        Devuelve la prioridad del documento.

        Devuelve
        -------
        int
            Devuelve 1 si el documento es urgente, 0 si no lo es.
        '''
        if self.urgente:
            self.prioridad = 1
        else:
            self.prioridad = 0
        return self.prioridad


# Objetos
documento1 = Documento(
    titulo='Informe de Ventas',
    descripcion='Informe detallado sobre las ventas del mes.'
)
documento2 = Documento(
    titulo='Planificación de Recursos',
    descripcion='Documento para la asignación de recursos en el proyecto.'
)
documento3 = Documento(
    titulo='Acta de Reunión',
    descripcion='Resumen de la reunión del comité de dirección.'
)
documento4 = Documento(
    titulo='Propuesta de Marketing',
    descripcion='Propuesta con estrategias para aumentar las ventas.'
)
documento5 = Documento(
    titulo='Informe de Finanzas',
    descripcion='Informe detallado sobre el estado financiero de la empresa.'
)

documento2.marcar_urgente()
documento4.marcar_urgente()
print(documento1.prioritarios())
print(documento2.prioritarios())
