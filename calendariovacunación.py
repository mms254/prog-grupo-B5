# calendario_vacunacion.py

from datetime import datetime


class CalendarioVacunacion:
    def __init__(self):
        # Definimos las vacunas por edad o tipo
        self.vacunas = {
            18: ["Vacuna Hepatitis B", "Vacuna Triple Viral"],
            60: ["Vacuna Neumocócica", "Vacuna Meningitis"],
            "menor": ["Vacuna DTP", "Vacuna Polio", "Vacuna MMR"],
            "alergico": ["Vacuna antialérgica", "Vacuna para asma"]
        }

    # Método para determinar la próxima vacuna según la edad y condiciones del paciente
    def obtener_vacunas(self, paciente):
        edad = paciente.edad
        alergias = paciente.alergias if hasattr(paciente, 'alergias') else None

        vacunas_recomendadas = []

        # Recomendaciones según edad
        if edad < 18:
            vacunas_recomendadas += self.vacunas["menor"]
        if edad >= 60:
            vacunas_recomendadas += self.vacunas[60]

        # Si tiene alergias
        if alergias and "alergia" in alergias:
            vacunas_recomendadas += self.vacunas["alergico"]

        # Recomendación según edad exacta
        if edad in self.vacunas:
            vacunas_recomendadas += self.vacunas[edad]

        return vacunas_recomendadas

    # Mostrar calendario de vacunación
    def mostrar_calendario(self, paciente):
        vacunas = self.obtener_vacunas(paciente)
        if vacunas:
            print(f"Calendario de vacunación para {paciente.nombre}:")
            for vacuna in vacunas:
                print(f"- {vacuna}")
        else:
            print(f"No hay vacunas recomendadas para {paciente.nombre} en este momento.")
