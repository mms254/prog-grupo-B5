class Persona:
    def __init__(self, id, nombre, apellido, edad, genero):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def a_diccionario(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'genero': self.genero
        }

    def __str__(self):
        return(f'ID: {self.id} - Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - Género {self.genero}')