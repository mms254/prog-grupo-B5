# main.py

from gestion_usuarios import GestionUsuarios
from calendario_vacunacion import CalendarioVacunacion
from paciente import Paciente
from medico import Medico
from habitacion import Habitacion

# Crear instancias
gestion_usuarios = GestionUsuarios()
calendario_vacunacion = CalendarioVacunacion()

# Crear pacientes
paciente1 = Paciente("P001", "Juan", "Pérez", 16, "M", "grave", alergias=["alergia"])
paciente2 = Paciente("P002", "Ana", "Martínez", 70, "F", "estable")

# Crear trabajadores
medico1 = Medico("MED001", "Carlos", "Gomez", 45, "M", "Día", "2020-01-01", 40, 3000, "Cardiología", 5)
habitacion1 = Habitacion(101, "UCI")

# Alta de pacientes y médicos
gestion_usuarios.alta_paciente(paciente1)
gestion_usuarios.alta_paciente(paciente2)
gestion_usuarios.alta_trabajador(medico1)

# Asignación de médico y habitación
gestion_usuarios.asignar_medico_paciente(paciente1, medico1)
gestion_usuarios.asignar_habitacion_paciente(paciente1, habitacion1)

# Mostrar pacientes
gestion_usuarios.listar_pacientes()

# Mostrar calendario de vacunación para paciente1
calendario_vacunacion.mostrar_calendario(paciente1)
