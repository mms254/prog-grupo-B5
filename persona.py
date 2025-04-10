import bcrypt as bcrypt

class Persona:
    '''
    Clase que representa a una persona, con atributos básicos como id, nombre, apellido, edad, genero,
    y rol. Además, incluye un atributo de password hashado para seguridad.

    Atributos:
    id (str): Identificador único de la persona.
    nombre (str): Nombre de la persona.
    apellido (str): Apellido de la persona.
    edad (int): Edad de la persona.
    genero (str): Género de la persona.
    password_hash (str): Contraseña hasheada de la persona.
    rol (str): Rol o puesto que ocupa la persona (por ejemplo, 'paciente', 'médico').

    Métodos:
    a_diccionario(): Devuelve un diccionario con los atributos básicos de la persona.
    verificar_password(password: str) -> bool: Verifica si la contraseña proporcionada coincide con el hash guardado.
    __str__(): Devuelve una cadena con la información básica de la persona.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str, rol: str, password: str):
        '''
        Inicializa una nueva instancia de la clase Persona.

        Parámetros:
        id (str): Identificador único de la persona.
        nombre (str): Nombre de la persona.
        apellido (str): Apellido de la persona.
        edad (int): Edad de la persona.
        genero (str): Género de la persona.
        rol (str): Rol o puesto que ocupa la persona (por ejemplo, 'paciente', 'médico').
        password (str): Contraseña de la persona. Se guardará como hash.
        '''
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.rol = rol

    def a_diccionario(self) -> dict:
        '''
        Convierte los atributos básicos de la persona en un diccionario.

        Devuelve:
        dict: Diccionario con los atributos básicos de la persona.
        '''
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'genero': self.genero
        }

    def verificar_password(self, password: str) -> bool:
        '''
        Verifica si la contraseña proporcionada coincide con el hash guardado.

        Parámetros:
        password (str): La contraseña a verificar.

        Devuelve:
        bool: True si la contraseña coincide con el hash, False de lo contrario.
        '''
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

    def __str__(self) -> str:
        '''
        Devuelve una representación en cadena de la persona.

        Devuelve:
        str: Una cadena con la información básica de la persona.
        '''
        return(f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero}')

# Creación de objetos de la clase Persona
persona1 = Persona(id='P001', nombre='Carlos', apellido='Crespo', edad=45, genero='Masculino', rol='paciente', password='password123')
persona2 = Persona(id='P002', nombre='Lucia', apellido='Monteagudo', edad=36, genero='Femenino', rol='paciente', password='password123')
persona3 = Persona(id='P003', nombre='Marcos', apellido='Hernandez', edad=60, genero='Masculino', rol='paciente', password='password123')
persona4 = Persona(id='P004', nombre='Daniel', apellido='Paredes', edad=52, genero='Masculino', rol='paciente', password='password123')
persona5 = Persona(id='P005', nombre='Mario', apellido='Morant', edad=28, genero='Masculino', rol='paciente', password='password123')
