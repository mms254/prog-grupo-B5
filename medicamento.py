from datetime import datetime

class Medicamento:
    '''
    Clase que representa un medicamento, con información sobre su nombre, dosis, precio, fecha de caducidad 
    y posibles alérgenos. Permite obtener información sobre el medicamento y verificar su caducidad.

    Atributos
    ----------
    nombre : str
        Nombre del medicamento.
    dosis : str
        Dosis recomendada del medicamento.
    precio : float
        Precio del medicamento.
    fecha_caducidad : date
        Fecha de caducidad del medicamento.
    alergenos : list, opcional
        Lista de alérgenos presentes en el medicamento. Por defecto es None.

    Métodos
    -------
    __init__(nombre: str, dosis: str, precio: float, fecha_caducidad: date, alergenos: list = None)
        Inicializa los atributos del medicamento.
    obtener_info() -> str
        Devuelve una cadena con la información del medicamento.
    verificar_caducidad() -> str
        Verifica si el medicamento ha caducado o no.
    '''

    def __init__(self, nombre: str, dosis: str, precio: float, fecha_caducidad: datetime, alergenos: list = None):
        '''
        Inicializa los atributos del medicamento, incluidos alérgenos si se proporcionan.

        Parámetros
        ----------
        nombre : str
            Nombre del medicamento.
        dosis : str
            Dosis recomendada del medicamento.
        precio : float
            Precio del medicamento.
        fecha_caducidad : date
            Fecha de caducidad del medicamento.
        alergenos : list, opcional
            Lista de alérgenos presentes en el medicamento. Por defecto es None.

        Excepciones
        ------------
        ValueError
            Si la fecha de caducidad no es válida.
        '''
        self.nombre = nombre
        self.dosis = dosis
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        if alergenos is not None:
            self.alergenos = alergenos
        else:
            self.alergenos = []
    def obtener_info(self) -> str:
        '''
        Devuelve la información del medicamento en formato de cadena.

        Devuelve
        -------
        str
            Información detallada sobre el medicamento.
        '''
        if self.alergenos:
            info = (f'Medicamento: {self.nombre}\n'
                f'Dosis: {self.dosis}\n'
                f'Precio: {self.precio}\n'
                f'Fecha de caducidad: {self.fecha_caducidad}\n'
                f'Alergenos: {self.alergenos} \n')
        else:
            info = (f'Medicamento: {self.nombre}\n'
                    f'Dosis: {self.dosis}\n'
                    f'Precio: {self.precio}\n'
                    f'Fecha de caducidad: {self.fecha_caducidad}\n'
                    f'Alergenos: Ninguno \n')
        return info

    def verificar_caducidad(self) -> str:
        '''
        Verifica si el medicamento ha caducado o no.

        Devuelve
        -------
        str
            Un mensaje indicando si el medicamento ha caducado o si está dentro de su periodo de validez.
        '''
        fecha_actual = datetime.now().date()
        if self.fecha_caducidad.date() < fecha_actual:
            return f'El medicamento {self.nombre} ha caducado el {self.fecha_caducidad}.'
        else:
            return f'El medicamento {self.nombre} está dentro de su periodo de validez.'


# Creación de objetos Medicamento con sus atributos
medicamento1 = Medicamento(
    nombre="Ibuprofeno",
    dosis="200mg",
    precio=5.50,
    fecha_caducidad=datetime(2025, 12, 31),
    alergenos=["Lactosa"]
)

medicamento2 = Medicamento(
    nombre="Paracetamol",
    dosis="500mg",
    precio=4.00,
    fecha_caducidad=datetime(2024, 5, 20)
)

medicamento3 = Medicamento(
    nombre="Amoxicilina",
    dosis="250mg",
    precio=8.00,
    fecha_caducidad=datetime(2025, 3, 15),
    alergenos=["Penicilina"]
)

medicamento4 = Medicamento(
    nombre="Aspirina",
    dosis="300mg",
    precio=3.50,
    fecha_caducidad=datetime(2024, 7, 5)
)

medicamento5 = Medicamento(
    nombre="Loratadina",
    dosis="10mg",
    precio=2.50,
    fecha_caducidad=datetime(2026, 1, 10),
    alergenos=["Sulfatos"]
)

print(medicamento2.obtener_info())
print(medicamento3.verificar_caducidad())
