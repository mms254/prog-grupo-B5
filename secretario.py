from trabajador import Trabajador
from documento import Documento


class Secretario(Trabajador, Documento):
    '''
    Clase que representa a un secretario, quien es un trabajador que maneja documentos
    y realiza tareas administrativas dentro de un departamento.

    Hereda de:
        - Trabajador: para obtener atributos relacionados con el trabajo.
        - Documento: para manejar y firmar documentos.

    Atributos
    ----------
    id : str
        El identificador único del secretario.
    nombre : str
        El nombre del secretario.
    apellido : str
        El apellido del secretario.
    edad : int
        La edad del secretario.
    genero : str
        El género del secretario.
    turno : str
        El turno en el que trabaja el secretario.
    horas : int
        Las horas laborales que realiza el secretario.
    salario : float
        El salario del secretario.
    titulo : str
        El título académico del secretario.
    descripcion : str
        Una breve descripción del trabajo o responsabilidades del secretario.
    antiguedad : int
        Los años de experiencia del secretario en la empresa.
    email : str
        El correo electrónico del secretario.
    departamento : str
        El departamento al que pertenece el secretario.

    Métodos
    -------
    firma_documentos(documento : Documento) -> str
        Permite al secretario firmar un documento si es una instancia de la clase Documento.

    enviar_correo(destinatario : str, asunto : str, mensaje : str) -> str
        Envía un correo electrónico con el asunto y el mensaje proporcionados al destinatario.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, turno: str, horas: int,salario: float, titulo: str, descripcion: str, antiguedad: int, email: str, departamento: str):
        '''
        Inicializa un nuevo objeto Secretario con la información proporcionada.

        Parámetros
        -----------
        id : str
            El identificador único del secretario.
        nombre : str
            El nombre del secretario.
        apellido : str
            El apellido del secretario.
        edad : int
            La edad del secretario.
        genero : str
            El género del secretario.
        turno : str
            El turno en el que trabaja el secretario.
        horas : int
            Las horas laborales que realiza el secretario.
        salario : float
            El salario del secretario.
        titulo : str
            El título académico del secretario.
        descripcion : str
            Una breve descripción del trabajo o responsabilidades del secretario.
        antiguedad : int
            Los años de experiencia del secretario en la empresa.
        email : str
            El correo electrónico del secretario.
        departamento : str
            El departamento al que pertenece el secretario.
        '''
        Trabajador.__init__(self, id, nombre, apellido, edad, genero, turno, horas, salario)
        Documento.__init__(self, titulo, descripcion)
        self.antiguedad = antiguedad
        self.email = email
        self.departamento = departamento

    def firma_documentos(self, documento: Documento) -> str:
        '''
        Permite al secretario firmar un documento.

        Parámetros
        -----------
        documento : Documento
            El documento que será firmado por el secretario.

        Excepciones
        ------------
        ValueError
            Si el parámetro `documento` no es una instancia de la clase Documento.

        Devuelve
        --------
        str
            Un mensaje confirmando que el documento ha sido firmado.
        '''
        if not isinstance(documento, Documento):
            raise ValueError('No has dado un documento')
        else:
            documento.firmar_documento(self.nombre)
            return f'Se ha firmado el documento {self.nombre}'

    def enviar_correo(self, destinatario: str, asunto: str, mensaje: str) -> str:
        '''
        Envía un correo electrónico con el asunto y mensaje proporcionados al destinatario.

        Parámetros
        -----------
        destinatario : str
            El destinatario del correo electrónico.
        asunto : str
            El asunto del correo electrónico.
        mensaje : str
            El cuerpo del mensaje del correo electrónico.

        Devuelve
        --------
        str
            Un mensaje confirmando que el correo ha sido enviado.
        '''
        return f'Correo enviado a {destinatario} con asunto "{asunto}" y mensaje: {mensaje}'

# Creación de los objetos de la clase Secretario

secretario1 = Secretario(
    id='SEC001',
    nombre='Ana',
    apellido='González',
    edad=28,
    genero='Femenino',
    turno='mañana',
    horas=40,
    salario=1500,
    titulo='Licenciatura en Administración',
    descripcion='Gestión de documentos y tareas administrativas',
    antiguedad=3,
    email='ana.gonzalez@empresa.com',
    departamento='Recursos Humanos'
)

secretario2 = Secretario(
    id='SEC002',
    nombre='Carlos',
    apellido='López',
    edad=35,
    genero='Masculino',
    turno='tarde',
    horas=38,
    salario=1600,
    titulo='Diplomado en Gestión Empresarial',
    descripcion='Atención al cliente y gestión de correspondencia',
    antiguedad=5,
    email='carlos.lopez@empresa.com',
    departamento='Atención al Cliente'
)

secretario3 = Secretario(
    id='SEC003',
    nombre='Beatriz',
    apellido='Martínez',
    edad=40,
    genero='Femenino',
    turno='mañana',
    horas=36,
    salario=1550,
    titulo='Licenciatura en Derecho',
    descripcion='Gestión de contratos y documentos legales',
    antiguedad=8,
    email='beatriz.martinez@empresa.com',
    departamento='Legal'
)

secretario4 = Secretario(
    id='SEC004',
    nombre='Luis',
    apellido='Pérez',
    edad=30,
    genero='Masculino',
    turno='noche',
    horas=40,
    salario=1700,
    titulo='Técnico en Administración de Empresas',
    descripcion='Soporte administrativo y gestión de agendas',
    antiguedad=4,
    email='luis.perez@empresa.com',
    departamento='Operaciones'
)

secretario5 = Secretario(
    id='SEC005',
    nombre='Elena',
    apellido='Rodríguez',
    edad=25,
    genero='Femenino',
    turno='tarde',
    horas=35,
    salario=1450,
    titulo='Bachillerato en Ciencias Sociales',
    descripcion='Asistencia administrativa y organización de eventos',
    antiguedad=2,
    email='elena.rodriguez@empresa.com',
    departamento='Marketing'
)
