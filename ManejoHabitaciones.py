# manejo_habitaciones.py
from habitacion import Habitacion
from enfermero import Enfermero
from paciente import Paciente
from typing import Dict, Optional, List, Union

class ManejoHabitaciones:
    """Clase para gestionar habitaciones, su asignación a enfermeros y pacientes.

    Esta clase permite agregar habitaciones al sistema, asignarlas a enfermeros, asignar pacientes
    a habitaciones, limpiar habitaciones y mostrar información sobre las habitaciones.

    Attributes:
        habitaciones (Dict[str, Habitacion]): Diccionario que mapea números de habitación a objetos Habitacion.
        enfermeros (Dict[str, Enfermero]): Diccionario que mapea números de habitación a enfermeros asignados.
    """
    def __init__(self) -> None:
        """Inicializa una nueva instancia de ManejoHabitaciones.

        Crea dos diccionarios vacíos para almacenar las habitaciones y los enfermeros asignados.
        """
        self.habitaciones: Dict[str, Habitacion] = {}  # Diccionario para almacenar habitaciones: {numero_habitacion: Habitacion}
        self.enfermeros: Dict[str, Enfermero] = {}     # Diccionario para almacenar enfermeros asignados: {numero_habitacion: Enfermero}

    def agregar_habitacion(self, habitacion: Habitacion) -> None:
        """Agrega una habitación al sistema.

        Args:
            habitacion (Habitacion): Objeto de tipo Habitacion a agregar al sistema.

        Raises:
            ValueError: Si el objeto no es una instancia de Habitacion o si la habitación ya está registrada.

        Example:
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo = ManejoHabitaciones()
            >>> manejo.agregar_habitacion(habitacion)
            Habitación 101 agregada al sistema
        """
        if not isinstance(habitacion, Habitacion):
            raise ValueError("El objeto debe ser una instancia de la clase Habitacion")
        if habitacion.numero_habitacion in self.habitaciones:
            raise ValueError(f"La habitación {habitacion.numero_habitacion} ya está registrada")
        self.habitaciones[habitacion.numero_habitacion] = habitacion
        print(f"Habitación {habitacion.numero_habitacion} agregada al sistema")

    def asignar_habitacion_a_enfermero(self, numero_habitacion: str, enfermero: Enfermero) -> None:
        """Asigna una habitación a un enfermero.

        Args:
            numero_habitacion (str): Número de la habitación a asignar.
            enfermero (Enfermero): Objeto de tipo Enfermero que se asignará a la habitación.

        Raises:
            ValueError: Si el objeto no es una instancia de Enfermero o si la habitación no está registrada.

        Example:
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo = ManejoHabitaciones()
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            Habitación 101 asignada al enfermero Ana Gómez
        """
        if not isinstance(enfermero, Enfermero):
            raise ValueError("El objeto debe ser una instancia de la clase Enfermero")
        if numero_habitacion not in self.habitaciones:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada en el sistema")
        self.enfermeros[numero_habitacion] = enfermero
        print(f"Habitación {numero_habitacion} asignada al enfermero {enfermero.nombre} {enfermero.apellido}")

    def limpiar_habitacion(self, numero_habitacion: str, enfermero: Enfermero) -> None:
        """Limpia una habitación específica, verificando que el enfermero esté asignado.

        Args:
            numero_habitacion (str): Número de la habitación a limpiar.
            enfermero (Enfermero): Objeto de tipo Enfermero que intenta limpiar la habitación.

        Raises:
            ValueError: Si la habitación no está registrada o si el enfermero no está asignado a la habitación.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            >>> manejo.limpiar_habitacion("101", enfermero)
        """
        habitacion: Optional[Habitacion] = self.buscar_habitacion(numero_habitacion)
        if not habitacion:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada")
        if numero_habitacion not in self.enfermeros or self.enfermeros[numero_habitacion] != enfermero:
            raise ValueError(f"La habitación {numero_habitacion} no está asignada al enfermero {enfermero.nombre}")
        habitacion.limpiar()

    def asignar_paciente_a_habitacion(self, paciente: Paciente, numero_habitacion: str, enfermero: Enfermero) -> None:
        """Asigna un paciente a una habitación específica, verificando limpieza y capacidad.

        Args:
            paciente (Paciente): Objeto de tipo Paciente a asignar a la habitación.
            numero_habitacion (str): Número de la habitación donde se asignará el paciente.
            enfermero (Enfermero): Objeto de tipo Enfermero que realiza la asignación.

        Raises:
            ValueError: Si la habitación no está registrada, no está asignada al enfermero,
                        no está limpia, o no tiene capacidad para más pacientes.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            >>> manejo.limpiar_habitacion("101", enfermero)
            >>> paciente = Paciente(id="PAC1", username="juan", password="contraseña123",
            ...                     nombre="Juan Pérez", edad=30)
            >>> manejo.asignar_paciente_a_habitacion(paciente, "101", enfermero)
            Paciente Juan Pérez asignado a la habitación 101
        """
        habitacion: Optional[Habitacion] = self.buscar_habitacion(numero_habitacion)
        if not habitacion:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada")
        if numero_habitacion not in self.enfermeros or self.enfermeros[numero_habitacion] != enfermero:
            raise ValueError(f"La habitación {numero_habitacion} no está asignada al enfermero {enfermero.nombre}")

        # Verificar si la habitación está limpia
        if not habitacion.limpia:
            raise ValueError(f"La habitación {numero_habitacion} no está limpia. Limpie la habitación antes de asignar pacientes.")

        # Asignar el paciente a la habitación
        habitacion.añadir_pacientes(paciente)
        print(f"Paciente {paciente.nombre} asignado a la habitación {numero_habitacion}")

        # Asignar el paciente al enfermero si no está asignado
        if paciente not in enfermero.pacientes_asignados:
            enfermero.asignar_paciente(paciente)

    def eliminar_paciente_de_habitacion(self, paciente: Paciente, numero_habitacion: str, enfermero: Enfermero) -> None:
        """Elimina un paciente de una habitación específica.

        Args:
            paciente (Paciente): Objeto de tipo Paciente a eliminar de la habitación.
            numero_habitacion (str): Número de la habitación de la que se eliminará el paciente.
            enfermero (Enfermero): Objeto de tipo Enfermero que realiza la eliminación.

        Raises:
            ValueError: Si la habitación no está registrada o no está asignada al enfermero.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            >>> manejo.limpiar_habitacion("101", enfermero)
            >>> paciente = Paciente(id="PAC1", username="juan", password="contraseña123",
            ...                     nombre="Juan Pérez", edad=30)
            >>> manejo.asignar_paciente_a_habitacion(paciente, "101", enfermero)
            >>> manejo.eliminar_paciente_de_habitacion(paciente, "101", enfermero)
        """
        habitacion: Optional[Habitacion] = self.buscar_habitacion(numero_habitacion)
        if not habitacion:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada")
        if numero_habitacion not in self.enfermeros or self.enfermeros[numero_habitacion] != enfermero:
            raise ValueError(f"La habitación {numero_habitacion} no está asignada al enfermero {enfermero.nombre}")
        habitacion.eliminar_paciente(paciente)

    def buscar_habitacion(self, numero_habitacion: str) -> Optional[Habitacion]:
        """Busca una habitación por su número.

        Args:
            numero_habitacion (str): Número de la habitación a buscar.

        Returns:
            Optional[Habitacion]: Objeto Habitacion si se encuentra, None en caso contrario.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> encontrada = manejo.buscar_habitacion("101")
            >>> encontrada.numero_habitacion
            '101'
        """
        return self.habitaciones.get(numero_habitacion)

    def mostrar_habitaciones(self, enfermero: Enfermero) -> str:
        """Muestra información de las habitaciones asignadas a un enfermero.

        Args:
            enfermero (Enfermero): Objeto de tipo Enfermero cuyas habitaciones asignadas se mostrarán.

        Returns:
            str: Cadena con la información de las habitaciones asignadas al enfermero.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            >>> print(manejo.mostrar_habitaciones(enfermero))
            Habitaciones asignadas:
            Habitacion: 101 - Limpia: False - Capacidad: 2 - Pacientes asignados: [] - Cantidad de pacientes: 0
        """
        habitaciones_asignadas: List[Habitacion] = [
            habitacion for num, habitacion in self.habitaciones.items()
            if num in self.enfermeros and self.enfermeros[num] == enfermero
        ]
        if not habitaciones_asignadas:
            return "No hay habitaciones asignadas a este enfermero"
        info: str = "Habitaciones asignadas:\n"
        for habitacion in habitaciones_asignadas:
            info += f"{habitacion.obtener_info()}\n"
        return info.rstrip('\n')

    def mostrar_todas_habitaciones(self) -> str:
        """Muestra información de todas las habitaciones en el sistema.

        Returns:
            str: Cadena con la información de todas las habitaciones y sus enfermeros asignados.

        Example:
            >>> manejo = ManejoHabitaciones()
            >>> habitacion = Habitacion(numero_habitacion="101", capacidad=2)
            >>> manejo.agregar_habitacion(habitacion)
            >>> enfermero = Enfermero(id="ENF1", username="ana", password="contraseña789",
            ...                       nombre="Ana", apellido="Gómez", edad=35, genero="Femenino",
            ...                       turno="noche", horas=40, salario=2000, especialidad="Cuidados Intensivos", antiguedad=5)
            >>> manejo.asignar_habitacion_a_enfermero("101", enfermero)
            >>> print(manejo.mostrar_todas_habitaciones())
            Habitaciones en el sistema:
            Habitacion: 101 - Limpia: False - Capacidad: 2 - Pacientes asignados: [] - Cantidad de pacientes: 0 - Enfermero asignado: Ana Gómez
        """
        if not self.habitaciones:
            return "No hay habitaciones registradas en el sistema"
        info: str = "Habitaciones en el sistema:\n"
        for habitacion in self.habitaciones.values():
            enfermero: Union[Enfermero, str] = self.enfermeros.get(habitacion.numero_habitacion, "Ninguno")
            if enfermero != "Ninguno":
                enfermero_info: str = f"{enfermero.nombre} {enfermero.apellido}"
            else:
                enfermero_info = "Ninguno"
            info += f"{habitacion.obtener_info()} - Enfermero asignado: {enfermero_info}\n"
        return info.rstrip('\n')