class Persona:
    '''
    Clase que representa a una persona dentro del sistema. Contiene información básica sobre la persona,
    como su ID, nombre, apellido, edad y género. Además, tiene métodos para convertir la persona a un diccionario
    y mostrar su representación en cadena.

    Atributos
    ----------
    id : str
        Identificador único de la persona.
    nombre : str
        Nombre de la persona.
    apellido : str
        Apellido de la persona.
    edad : int
        Edad de la persona.
    genero : str
        Género de la persona.

    Métodos
    -------
    __init__(id: str, nombre: str, apellido: str, edad: int, genero: str) -> None
        Inicializa los atributos de la persona.

    a_diccionario() -> dict
        Devuelve un diccionario con los atributos de la persona.

    __str__() -> str
        Devuelve una cadena representando la persona.
    '''

    def __init__(self, id: str, nombre: str, apellido: str, edad: int, genero: str) -> None:
        '''
        Inicializa los atributos de la persona.

        Parámetros
        ----------
        id : str
            Identificador único de la persona.
        nombre : str
            Nombre de la persona.
        apellido : str
            Apellido de la persona.
        edad : int
            Edad de la persona.
        genero : str
            Género de la persona.
        '''
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def a_diccionario(self) -> dict:
        '''
        Devuelve un diccionario con los atributos de la persona.

        Devuelve
        -------
        dict
            Diccionario con los atributos de la persona.
        '''
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'genero': self.genero
        }

    def __str__(self) -> str:
        '''
        Devuelve una cadena representando la persona.

        Devuelve
        -------
        str
            Información sobre la persona en formato de cadena.
        '''
        return(f'ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Género: {self.genero}')

# Creación de objetos de la clase Persona
persona1 = Persona(id='P001', nombre='Carlos', apellido='Crespo', edad=45, genero='Masculino')
persona2 = Persona(id='P002', nombre='Lucia', apellido='Monteagudo', edad=36, genero='Femenino')
persona3 = Persona(id='P003', nombre='Marcos', apellido='Hernandez', edad=60, genero='Masculino')
persona4 = Persona(id='P004', nombre='Daniel', apellido='Paredes', edad=52, genero='Masculino')
persona5 = Persona(id='P005', nombre='Mario', apellido='Morant', edad=28, genero='Masculino')
