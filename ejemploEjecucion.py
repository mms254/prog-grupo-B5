""" Este archivo no sirve para nada, solo para ver que mi código funciona correctamente"""


from paciente import Paciente
from gestorCitas import GestorCitas, CitaPresencial, CitaTelefonica, CitaUrgencias

def main():
    paciente1 = Paciente(1, "Juan", "Pérez", 35, "M", "estable", None)
    gestor = GestorCitas()

    # Crear diferentes tipos de citas
    cita_presencial = CitaPresencial(
        id_cita=101,
        paciente=paciente1,
        medico="Dr. García",
        fecha="2025-05-01",
        hora="10:00",
        centro="Centro de Salud Central"
    )

    cita_telefonica = CitaTelefonica(
        id_cita=102,
        paciente=paciente1,
        medico="Dra. López",
        fecha="2025-05-02",
        hora="11:00",
        telefono_contacto="555-123456"
    )

    cita_urgencias = CitaUrgencias(
        id_cita=103,
        paciente=paciente1,
        medico="Dr. Hernández",
        fecha="2025-05-03",
        hora="12:00",
        nivel_prioridad="alta"
    )

    # Añadir las citas al gestor
    gestor.añadir_cita(cita_presencial)
    gestor.añadir_cita(cita_telefonica)
    gestor.añadir_cita(cita_urgencias)

    # Mostrar todas las citas creadas
    print("Listado de citas:")
    gestor.mostrar_citas()

    # Cancelar la cita telefónica (id_cita=102)
    print("\nCancelando la cita con ID 102:")
    resultado_cancelar = gestor.cancelar_cita(102)
    print(resultado_cancelar)

    # Marcar la cita presencial (id_cita=101) como atendida
    print("\nAtendiendo la cita con ID 101:")
    resultado_atender = gestor.atender_cita(101)
    print(resultado_atender)

    # Mostrar el listado actualizado de citas
    print("\nListado actualizado de citas:")
    gestor.mostrar_citas()

    print("\nAñadiendo nueva cita usando el operador '+='")
    nueva_cita = CitaPresencial(
        id_cita = 104,
        paciente = paciente1,
        medico = "Dr.Ramírez",
        fecha = "2025-05-04",
        hora = "09:30",
        centro = "Clínica Norte"
    )

    gestor += nueva_cita

    print("Mostrar citas actualizada:")
    gestor.mostrar_citas()


main()
