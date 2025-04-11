"""
API para la gestión de usuarios y SIPs en un sistema de salud.

Esta API incluye:
- Endpoints para gestionar SIPs (Sistema de Identificación de Pacientes).
- Integración con la API RxNorm para obtener información sobre medicamentos.
- Gestión de usuarios (pacientes, médicos, enfermeros, auxiliares) con autenticación.
- Endpoints para asignar médicos, habitaciones y listar pacientes/trabajadores.
"""

# === Importaciones ===
from flask import Flask, request, jsonify
from functools import wraps
import requests
import uuid
from typing import Dict, Any

from auxiliar import Auxiliar
from enfermero import Enfermero
from medico import Medico
from paciente import Paciente
from habitacion import Habitacion
from pdf_generator import generar_pdf_paciente

# === Configuración de la Aplicación ===
app = Flask(__name__)

# URL de la API RxNorm para consultar medicamentos
RXNORM_URL = "https://rxnav.nlm.nih.gov/REST/drugs.json"

# === Base de Datos en Memoria ===
# Diccionarios para almacenar datos en memoria (SIPs, pacientes, trabajadores)
sips: Dict[str, str] = {}  # Almacena los SIPs de los pacientes
pacientes: Dict[str, Any] = {}  # Almacena pacientes
medicos: Dict[str, Any] = {}  # Almacena médicos
enfermeros: Dict[str, Any] = {}  # Almacena enfermeros
auxiliares: Dict[str, Any] = {}  # Almacena auxiliares

# Diccionario para simular usuarios registrados (en lugar de una base de datos)
usuarios_registrados = {
    "juan": {"password": "pepe123", "rol": "paciente"},
    "ana": {"password": "med123", "rol": "medico"},
    "luis": {"password": "enf123", "rol": "enfermero"}
}

# === Decorador de Autenticación ===
def requiere_autenticacion(f):
    """
    Decorador que verifica la autenticación básica (usuario y contraseña) en la solicitud.
    Usa un diccionario en memoria para validar los usuarios.
    Si las credenciales son válidas, pasa un objeto usuario con el rol al endpoint.
    Si no, devuelve un error 401 (Unauthorized).
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Obtener las credenciales de autenticación básica de la solicitud
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({"detail": "Autenticación requerida. Proporcione usuario y contraseña."}), 401

        # Buscar el usuario en el diccionario de usuarios registrados
        usuario = usuarios_registrados.get(auth.username)
        if not usuario:
            return jsonify({"detail": "Usuario no encontrado."}), 401

        # Verificar la contraseña
        if usuario["password"] != auth.password:
            return jsonify({"detail": "Contraseña incorrecta."}), 401

        # Crear un objeto usuario con el rol
        class UsuarioTemporal:
            def __init__(self, rol):
                self.rol = rol

        usuario_obj = UsuarioTemporal(usuario["rol"])
        return f(usuario_obj, *args, **kwargs)

    return decorated_function

# === Funciones de Utilidad para RxNorm ===
def obtener_informacion_medicamento(medicamento: str) -> None:
    """
    Consulta información de un medicamento usando la API RxNorm y la imprime.

    Parámetros
    ----------
    medicamento : str
        Nombre del medicamento a consultar.

    Ejemplo
    -------
    >>> obtener_informacion_medicamento("ibuprofeno")
    Nombre: Ibuprofen
    RXCUI: 5640
    TTY: IN
    Idioma: ENG
    -------------------------------
    """
    try:
        # Realizar la solicitud a la API RxNorm
        response = requests.get(RXNORM_URL, params={'name': medicamento})
        response.raise_for_status()  # Verifica si la solicitud fue exitosa

        # Parsear la respuesta JSON
        data = response.json()

        # Verificar si hay información de medicamentos
        if 'conceptGroup' not in data['drugGroup']:
            raise NameError('El medicamento no existe o no se encuentra en la base de datos.')

        medicamentos = data['drugGroup']['conceptGroup']
        for med in medicamentos:
            if 'conceptProperties' in med:
                for propiedad in med['conceptProperties']:
                    print(f"Nombre: {propiedad.get('name')}")
                    print(f"RXCUI: {propiedad.get('rxcui')}")
                    print(f"TTY: {propiedad.get('tty')}")
                    print(f"Idioma: {propiedad.get('language')}")
                    print("-------------------------------")
                    print("")

    except requests.exceptions.RequestException as error:
        print(f"No se puede completar la solicitud: {error}")
    except NameError as error:
        print(f"Error: {error}")

# === Funciones de Utilidad para SIPs ===
def generar_sip(paciente_id: str) -> str:
    """
    Genera un SIP único para el paciente.

    Parámetros
    ----------
    paciente_id : str
        Identificador único del paciente.

    Devuelve
    --------
    str
        SIP generado en formato 'SIP-<código_hexadecimal>'.
    """
    sip = f"SIP-{uuid.uuid4().hex[:10].upper()}"  # Genera un SIP único
    sips[paciente_id] = sip
    return sip

# === Endpoints de SIPs ===
@app.route('/')
def bienvenida():
    """Ruta principal que da la bienvenida al sistema."""
    return jsonify({
        "mensaje": (
            "Bienvenido/a al sistema generador de SIPs. "
            "Use /crear_sip/<id_paciente> para generar un SIP y "
            "/consultar_sip/<id_paciente> para consultar un SIP."
        )
    })

@app.route('/crear_sip/<paciente_id>', methods=['GET'])
def crear_sip(paciente_id: str):
    """
    Crea un SIP para el paciente especificado por su ID.

    Parámetros
    ----------
    paciente_id : str
        Identificador del paciente.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    if paciente_id in sips:
        return jsonify({"mensaje": "El paciente ya tiene un SIP asignado", "sip": sips[paciente_id]}), 400
    sip = generar_sip(paciente_id)
    return jsonify({"mensaje": "SIP creado correctamente", "sip": sip})

@app.route('/consultar_sip/<paciente_id>', methods=['GET'])
def consultar_sip(paciente_id: str):
    """
    Consulta el SIP asignado a un paciente por su ID.

    Parámetros
    ----------
    paciente_id : str
        Identificador del paciente.

    Devuelve
    --------
    jsonify
        SIP del paciente o mensaje de error.
    """
    sip = sips.get(paciente_id)
    if sip:
        return jsonify({"paciente_id": paciente_id, "sip": sip})
    return jsonify({"mensaje": "No se encontró el SIP para ese paciente"}), 404

# === Endpoints de Gestión de Usuarios ===
@app.route("/menu", methods=["GET"])
@requiere_autenticacion
def menu_usuario(usuario):
    """
    Devuelve un menú de opciones según el rol del usuario autenticado.

    Parámetros
    ----------
    usuario : object
        Objeto con el rol del usuario autenticado.

    Devuelve
    --------
    jsonify
        Menú de opciones según el rol.
    """
    if usuario.rol == "paciente":
        menu = [
            "1. Ver información personal",
            "2. Pedir cita",
            "3. Descargar información en PDF",
            "4. Recomendar medicamento según síntomas",
            "5. Ver citas",
            "6. Salir"
        ]
        return jsonify({"rol": "paciente", "menu": menu}), 200
    elif usuario.rol == "medico":
        menu = [
            "1. Ver lista de pacientes",
            "2. Ver citas",
            "3. Agregar entrada al historial médico de un paciente",
            "4. Salir"
        ]
        return jsonify({"rol": "medico", "menu": menu}), 200
    elif usuario.rol == "enfermero":
        menu = [
            "1. Ver habitaciones asignadas",
            "2. Asignar paciente a habitación",
            "3. Limpiar habitación",
            "4. Ver pacientes asignados",
            "5. Agregar nueva habitación",
            "6. Asignar habitación a este enfermero",
            "7. Eliminar paciente de habitación",
            "8. Salir"
        ]
        return jsonify({"rol": "enfermero", "menu": menu}), 200
    else:
        return jsonify({"detail": "Rol no reconocido"}), 403

@app.route('/pacientes', methods=['GET'])
def listar_pacientes():
    """
    Lista todos los pacientes activos.

    Devuelve
    --------
    jsonify
        Lista de pacientes.
    """
    resultado = []
    for p in pacientes.values():
        resultado.append({
            "nombre": p.nombre,
            "apellido": p.apellido,
            "estado": p.estado,
            "medico_asignado": p.medico_asignado.nombre if p.medico_asignado else "No asignado"
        })
    return jsonify(resultado)

@app.route('/pacientes/alta', methods=['POST'])
def alta_paciente():
    """
    Da de alta un nuevo paciente.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación.
    """
    try:
        data = request.json
        paciente = Paciente(**data)
        pacientes[paciente.id] = paciente
        return jsonify({"mensaje": f"Paciente {paciente.nombre} {paciente.apellido} dado de alta."})
    except Exception as e:
        return jsonify({"error": f"Error al dar de alta al paciente: {str(e)}"}), 400

@app.route('/pacientes/baja/<id_paciente>', methods=['DELETE'])
def baja_paciente(id_paciente: str):
    """
    Da de baja a un paciente por su ID.

    Parámetros
    ----------
    id_paciente : str
        Identificador del paciente.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    if id_paciente in pacientes:
        del pacientes[id_paciente]
        return jsonify({"mensaje": f"Paciente con ID {id_paciente} dado de baja."})
    return jsonify({"error": "Paciente no encontrado"}), 404

@app.route('/pacientes/asignar_medico', methods=['POST'])
def asignar_medico_paciente():
    """
    Asigna un médico a un paciente.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    data = request.json
    id_paciente = data.get('id_paciente')
    id_medico = data.get('id_medico')

    paciente = pacientes.get(id_paciente)
    medico = medicos.get(id_medico)

    if not paciente or not medico:
        return jsonify({"error": "Paciente o médico no encontrado"}), 404

    paciente.medico_asignado = medico
    return jsonify({"mensaje": f"Paciente {paciente.nombre} asignado a médico {medico.nombre}."})

@app.route('/pacientes/asignar_habitacion', methods=['POST'])
def asignar_habitacion_paciente():
    """
    Asigna una habitación a un paciente.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    data = request.json
    id_paciente = data.get('id_paciente')
    numero_habitacion = data.get('numero')

    paciente = pacientes.get(id_paciente)
    if not paciente:
        return jsonify({"error": "Paciente no encontrado"}), 404


    habitacion = Habitacion(numero=numero_habitacion)
    paciente.habitacion_asignada = habitacion
    return jsonify({"mensaje": f"Paciente {paciente.nombre} asignado a la habitación {habitacion.numero}."})

@app.route('/trabajadores/alta', methods=['POST'])
def alta_trabajador():
    """
    Da de alta un nuevo trabajador (médico, enfermero o auxiliar).

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    data = request.json
    rol = data.get('rol')

    try:
        if rol == 'medico':
            trabajador = Medico(**data)
            medicos[trabajador.id] = trabajador
        elif rol == 'enfermero':
            trabajador = Enfermero(**data)
            enfermeros[trabajador.id] = trabajador
        elif rol == 'auxiliar':
            trabajador = Auxiliar(**data)
            auxiliares[trabajador.id] = trabajador
        else:
            return jsonify({"error": "Rol no válido"}), 400
        return jsonify({"mensaje": f"Trabajador {trabajador.nombre} {trabajador.apellido} dado de alta."})
    except Exception as e:
        return jsonify({"error": f"Error al dar de alta al trabajador: {str(e)}"}), 400

@app.route('/trabajadores/baja/<id_trabajador>', methods=['DELETE'])
def baja_trabajador(id_trabajador: str):
    """
    Da de baja a un trabajador por su ID.

    Parámetros
    ----------
    id_trabajador : str
        Identificador del trabajador.

    Devuelve
    --------
    jsonify
        Mensaje de confirmación o error.
    """
    if id_trabajador in medicos:
        del medicos[id_trabajador]
    elif id_trabajador in enfermeros:
        del enfermeros[id_trabajador]
    elif id_trabajador in auxiliares:
        del auxiliares[id_trabajador]
    else:
        return jsonify({"error": "Trabajador no encontrado"}), 404
    return jsonify({"mensaje": f"Trabajador con ID {id_trabajador} dado de baja."})

@app.route('/trabajadores', methods=['GET'])
def listar_trabajadores():
    """
    Lista todos los trabajadores clasificados por tipo.

    Devuelve
    --------
    jsonify
        Lista de trabajadores.
    """
    return jsonify({
        "medicos": [str(m) for m in medicos.values()],
        "enfermeros": [str(e) for e in enfermeros.values()],
        "auxiliares": [str(a) for a in auxiliares.values()]
    })

@app.route("/paciente/descargar_pdf", methods=["GET"])
@requiere_autenticacion
def descargar_pdf(usuario):
    """
    Genera un PDF con la información del paciente autenticado.

    Parámetros
    ----------
    usuario : object
        Objeto con el rol del usuario autenticado.

    Devuelve
    --------
    jsonify
        Mensaje con el nombre del PDF generado o error.
    """
    if usuario.rol != "paciente":
        return jsonify({"detail": "Acceso denegado"}), 403

    try:
        nombre_pdf = generar_pdf_paciente(usuario)
        return jsonify({"message": f"PDF generado: {nombre_pdf}"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al generar el PDF: {str(e)}"}), 500

# === Endpoint de Prueba ===
@app.route("/test", methods=["GET"])
def test():
    """Endpoint de prueba para verificar que la API está funcionando."""
    return jsonify({"mensaje": "API funcionando correctamente"}), 200

# === Iniciar la Aplicación ===
if __name__ == "__main__":
    app.run(debug=True, port=5000)