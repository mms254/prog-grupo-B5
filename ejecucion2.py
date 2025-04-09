""" Este archivo no sirve para nada, solo para ver que mi código funciona correctamente """

from medico import Medico
from paciente import Paciente
from asignacion import Asignaciones

# Crear médicos
medico1 = Medico("MED001", "Sofía", "Ruiz", 45, "F", "Día", "2020-01-01", 8, 5000, "Cardiología", 8)
medico2 = Medico("MED002", "Diego", "López", 50, "M", "Noche", "2015-06-01", 10, 5500, "Clínico", 12)

# Crear pacientes
paciente1 = Paciente("PAC001", "Laura", "García", 30, "F", "Control general")
paciente2 = Paciente("PAC002", "Andrés", "Martínez", 42, "M", "Dolor de cabeza")
paciente3 = Paciente("PAC003", "Camila", "Fernández", 27, "F", "Chequeo anual")

# Crear instancia del gestor de asignaciones
gestor = Asignaciones(medicos=[medico1, medico2], pacientes=[paciente1, paciente2, paciente3])

# Asignar médicos a los pacientes
gestor.asignar(paciente1)
gestor.asignar(paciente2)
gestor.asignar(paciente3)

# Cambiar disponibilidad de un médico
gestor.cambiar_disponibilidad("MED001", False)

# Mostrar todas las asignaciones realizadas
gestor.mostrar_asignaciones()

