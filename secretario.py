from trabajador import Trabajador
from documento import Documento

class Secretario (Trabajador, Documento):
    def __init__(self, id, nombre, apellido, edad, genero, turno, horas, salario, titulo, descripcion, antiguedad, email, departamento):
        super().__init__(id, nombre, apellido, edad, genero, turno, horas, salario, titulo, descripcion)
        self.antiguedad = antiguedad
        self.email = email
        self.departamento = departamento

    def firma_documentos(self, documento):
        if not isinstance(documento, Documento):
            raise ValueError('No has dado un documento')
        else:
            documento.firmar_documento(self.nombre)
            return f'Se ha firmado el documento {self.nombre}'

    def enviar_correo(self, destinatario, asunto, mensaje):
        return f'Correo enviado a {destinatario} con asunto {asunto}"y mensaje: {mensaje}'
