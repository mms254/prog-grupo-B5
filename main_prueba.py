# main.py
# simulamos el funcioanmiento de la gestión de usuario y
# calendario de vacunación
# imprtamos las clases necesarias
from gestion_usuarios import GestionUsuarios
from calendario_vacunacion import CalendarioVacunacion
from paciente import Paciente
from medico import Medico
from habitacion import Habitacion

# Crear instancias
# creamos objetos de gestionusuarios y calendariovacunacion
# con estas instancias podremos dar de alta pacientes/trabajadores, asignamos roles y consultamos vacunas

gestion_usuarios = GestionUsuarios()
calendario_vacunacion = CalendarioVacunacion()

# Crear pacientes
# dos objetos:
#-paciente1- adolescente con alergias y estado grave
#-paciente2-paciente anciana de 70 años,estable,sin alergias
paciente1 = Paciente("P001", "Juan", "Pérez", 16, "M", "grave", alergias=["alergia"])
paciente2 = Paciente("P002", "Ana", "Martínez", 70, "F", "estable")

# Crear trabajadores
# medico1:objeto de tipo medico con atributos como turno, salario, especialidad...
# habitacion1: una habitacion en la unidad de cuidados intensivos la uci
medico1 = Medico("MED001", "Carlos", "Gomez", 45, "M", "Día", "2020-01-01", 40, 3000, "Cardiología", 5)
habitacion1 = Habitacion(101, "UCI")

# Alta de pacientes y médicos
# llama al método alta_paciente() para registrar los pacientes en el sistema
# llama a alta_trabajador() para registrar al médico en la base de datos trabajadores

gestion_usuarios.alta_paciente(paciente1)
gestion_usuarios.alta_paciente(paciente2)
gestion_usuarios.alta_trabajador(medico1)

# Asignación de médico y habitación
# paciente1 es asignaedo a medico1 como su medico responsable
# paciente1 también recibe una habitación en la uci
gestion_usuarios.asignar_medico_paciente(paciente1, medico1)
gestion_usuarios.asignar_habitacion_paciente(paciente1, habitacion1)

# Mostrar pacientes
# imprimimos la información básica de cada paciente activo en el sistema
# como nombre estado de salud y médico asignado
gestion_usuarios.listar_pacientes()

# Mostrar calendario de vacunación para paciente1
# este método evalúa la edad y alergias del paciente1 y muestra las vacunas
# que le corresponden según esas condiciones

calendario_vacunacion.mostrar_calendario(paciente1)
rog