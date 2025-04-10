# manejo_habitaciones.py
from habitacion import Habitacion
from enfermero import Enfermero

class ManejoHabitaciones:
    def __init__(self):
        self.habitaciones = {}  # Diccionario para almacenar habitaciones: {numero_habitacion: Habitacion}
        self.enfermeros = {}    # Diccionario para almacenar enfermeros asignados: {numero_habitacion: Enfermero}

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al sistema."""
        if not isinstance(habitacion, Habitacion):
            raise ValueError("El objeto debe ser una instancia de la clase Habitacion")
        if habitacion.numero_habitacion in self.habitaciones:
            raise ValueError(f"La habitación {habitacion.numero_habitacion} ya está registrada")
        self.habitaciones[habitacion.numero_habitacion] = habitacion
        print(f"Habitación {habitacion.numero_habitacion} agregada al sistema")

    def asignar_habitacion_a_enfermero(self, numero_habitacion, enfermero):
        """Asigna una habitación a un enfermero."""
        if not isinstance(enfermero, Enfermero):
            raise ValueError("El objeto debe ser una instancia de la clase Enfermero")
        if numero_habitacion not in self.habitaciones:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada en el sistema")
        self.enfermeros[numero_habitacion] = enfermero
        print(f"Habitación {numero_habitacion} asignada al enfermero {enfermero.nombre} {enfermero.apellido}")

    def limpiar_habitacion(self, numero_habitacion, enfermero):
        """Limpia una habitación específica, verificando que el enfermero esté asignado."""
        habitacion = self.buscar_habitacion(numero_habitacion)
        if not habitacion:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada")
        if numero_habitacion not in self.enfermeros or self.enfermeros[numero_habitacion] != enfermero:
            raise ValueError(f"La habitación {numero_habitacion} no está asignada al enfermero {enfermero.nombre}")
        habitacion.limpiar()

    def asignar_paciente_a_habitacion(self, paciente, numero_habitacion, enfermero):
        """Asigna un paciente a una habitación específica, verificando limpieza y capacidad."""
        habitacion = self.buscar_habitacion(numero_habitacion)
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

    def eliminar_paciente_de_habitacion(self, paciente, numero_habitacion, enfermero):
        """Elimina un paciente de una habitación específica."""
        habitacion = self.buscar_habitacion(numero_habitacion)
        if not habitacion:
            raise ValueError(f"La habitación {numero_habitacion} no está registrada")
        if numero_habitacion not in self.enfermeros or self.enfermeros[numero_habitacion] != enfermero:
            raise ValueError(f"La habitación {numero_habitacion} no está asignada al enfermero {enfermero.nombre}")
        habitacion.eliminar_paciente(paciente)

    def buscar_habitacion(self, numero_habitacion):
        """Busca una habitación por su número."""
        return self.habitaciones.get(numero_habitacion)

    def mostrar_habitaciones(self, enfermero):
        """Muestra información de las habitaciones asignadas a un enfermero."""
        habitaciones_asignadas = [
            habitacion for num, habitacion in self.habitaciones.items()
            if num in self.enfermeros and self.enfermeros[num] == enfermero
        ]
        if not habitaciones_asignadas:
            return "No hay habitaciones asignadas a este enfermero"
        info = "Habitaciones asignadas:\n"
        for habitacion in habitaciones_asignadas:
            info += f"{habitacion.obtener_info()}\n"
        return info.rstrip('\n')

    def mostrar_todas_habitaciones(self):
        """Muestra información de todas las habitaciones en el sistema."""
        if not self.habitaciones:
            return "No hay habitaciones registradas en el sistema"
        info = "Habitaciones en el sistema:\n"
        for habitacion in self.habitaciones.values():
            enfermero = self.enfermeros.get(habitacion.numero_habitacion, "Ninguno")
            if enfermero != "Ninguno":
                enfermero_info = f"{enfermero.nombre} {enfermero.apellido}"
            else:
                enfermero_info = "Ninguno"
            info += f"{habitacion.obtener_info()} - Enfermero asignado: {enfermero_info}\n"
        return info.rstrip('\n')