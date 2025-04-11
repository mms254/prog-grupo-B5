import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from paciente import Paciente
from typing import  List

def generar_pdf_paciente(paciente: Paciente) -> str:
    """Genera un archivo PDF con la información personal del paciente.

    Args:
        paciente (Paciente): Objeto de tipo Paciente que contiene la información a incluir en el PDF.

    Returns:
        str: Nombre del archivo PDF generado.

    Raises:
        IOError: Si hay un problema al escribir el archivo PDF en el disco.
        AttributeError: Si el objeto paciente no tiene los atributos esperados.
    """
    # Crear un directorio para los PDFs si no existe
    directorio_informes: str = "informes"
    if not os.path.exists(directorio_informes):
        os.makedirs(directorio_informes)

    # Generar el nombre del archivo PDF
    nombre_archivo: str = os.path.join(directorio_informes, f"Informe del Paciente_{paciente.id, paciente.username}.pdf")
    c: canvas.Canvas = canvas.Canvas(nombre_archivo, pagesize=letter)
    width: float
    height: float
    width, height = letter

    # Resto del código igual que antes...
    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Informe Personal del Paciente")

    # Información personal del paciente
    c.setFont("Helvetica", 12)
    y: float = height - 100
    c.drawString(100, y, f"Nombre: {getattr(paciente, 'nombre', 'No disponible')}")
    y -= 20
    c.drawString(100, y, f"Edad: {getattr(paciente, 'edad', 'No disponible')}")
    y -= 20
    medico_asignado: str = getattr(paciente, 'medico_asignado', 'No asignado')
    c.drawString(100, y, f"Médico Asignado: {medico_asignado}")
    y -= 20
    enfermedades: str = ", ".join(getattr(paciente, 'enfermedades', [])) if getattr(paciente, 'enfermedades', []) else "Ninguna"
    c.drawString(100, y, f"Enfermedades: {enfermedades}")
    y -= 20
    prioridad: str = getattr(paciente, 'prioridad_urgencias', 'No especificada')
    c.drawString(100, y, f"Tipo de Prioridad en Urgencias: {prioridad}")
    y -= 20
    habitacion: str = getattr(paciente, 'habitacion_asignada', 'No asignada')
    c.drawString(100, y, f"Habitación Asignada: {habitacion}")

    # Historial médico
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Historial Médico")
    c.setFont("Helvetica", 12)
    y -= 20
    historial_medico: List[str] = getattr(paciente, 'historial_medico', [])
    if historial_medico:
        for entrada in historial_medico:
            c.drawString(100, y, entrada)
            y -= 20
    else:
        c.drawString(100, y, "No hay entradas en el historial médico.")
        y -= 20

    # Citas
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y, "Citas")
    c.setFont("Helvetica", 12)
    y -= 20
    citas: List['Cita'] = getattr(paciente, 'citas', [])
    if citas:
        for cita in citas:
            c.drawString(100, y, f"Fecha: {cita.fecha_hora}, Médico: {cita.medico}, Motivo: {cita.motivo}")
            y -= 20
    else:
        c.drawString(100, y, "No hay citas programadas.")
        y -= 20

    c.save()
    return nombre_archivo