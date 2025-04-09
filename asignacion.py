import random
from typing import List
from medico import Medico
from paciente import Paciente

class Asignaciones:

    """
    Clase encargada de gestionar la asignación de médicos a paciente

    """

    def __init__(self, medicos : List[Medico], pacientes: List[Paciente]):

        """
            Parámetros:
            -----------

            Inicializa el gestor con una lista de médicos disponibles

            medicos: Lista de instancias de la clase Médico
            pacientes: Lista de instancias de la clase Paciente

        """
        self.medicos = medicos
        self.pacientes = pacientes
        self.asignaciones = {}

    def cambiar_disponibilidad(self, medico_id :str, disponible :bool) -> None:

        """
                Cambia la disponibilidad de un médico dado su ID.

                medico_id: ID del médico al que se desea cambiar la disponibilidad.
                disponible: True si el médico debe estar disponible, False si no.
        """
        for medico in self.medicos:
            if medico.id == medico_id:
                medico.disponibilidad = disponible
                print(f"La disponibilidad del médico {medico.nombre} ha sido actualizada.")
                return

            print("No se encontró un médico con ese ID.")

    def medicos_disponibles(self) -> List[Medico]:

        """
            Devuelve una lista con los médicos disponibles

        """
        disponibles = []
        for medico in self.medicos:
            if medico.disponibilidad:
                disponibles.append(medico)
        return disponibles

    def asignar(self, paciente : Paciente) -> bool:

        """
            Asigna aleatoriamente un médico disponible a un paciente.
            Retorna True si se realizó la asignación con éxito

        """

        disponibles = self.medicos_disponibles()
        if not disponibles:
            print(f"No hay médicos disponibles para el paciente {paciente.nombre}")
            return False

        medico = random.choice(disponibles)
        self.asignaciones[paciente.id] = medico.id

        print(f"Paciente {paciente.nombre} ha sido asignado al médico {medico.nombre}")


    def mostrar_asignaciones(self) -> None:

        """
            Muestra todas las asignaciones realizadas

        """

        if not self.asignaciones:
            print('No hay asignaciones para el paciente')
            return

        print("Lista de asignaciones:")
        for pac_id , med_id in self.asignaciones.items():
            print(f"Paciente ID :{pac_id} -> Médico Id {med_id}")