"""
Esta parte del código maneja una API que utilizaremos para la gestión de medicamentos. La API que utilizaremos se llama RxNorm.

RxNorm es una API médica estadounidense, mantenida por la NLM (National Library of Medicine). Si bien no proporciona apenas medicamentos
de otros países, la gran mayoría de objetos que necesitamos (por no decir todos) los encontraremos aquí. Es especialmente útil para
recibir información sobre medicamentos, como su uso clínico o su nombre estandarizado.


Para que funcione, se debe importar la librería requests.
"""

import requests

URL='https://rxnav.nlm.nih.gov/REST/drugs.json' #defino la url que voy a utilizar

def obtener_informacion(medicamento: str) -> None:
    """
    Esta función recoge el nombre de un medicamento e imprime una gran cantidad de información almacenada en la base de datos
    de la API. Gracias a la API, no hay que escribir el nombre exacto de un medicamento, ya que lo detecta por nombres similares o
    al escribirlo en español en lugar de en inglés.

    Parámetros:
    ---------
    medicamento: str
    nombre del medicamento del que queremos obtener la información.
    """

    try: #probamos
        informacion = requests.get(URL, params = {'name': medicamento})
        informacion.raise_for_status() #esta línea es muy importante para ver si ha funcionado correctamente la URL

        info_contenida= informacion.json() #guardamos la información que tenemos en la URL en formato json

        if 'conceptGroup' in info_contenida['drugGroup']:
            """
            esta línea es complicada y requiere explicación. Tanto lo de "drugGroup" como "conceptGroup" lo encontramos en la API
            que hemos implementado.
            Indagando en la documentación de la API, encontramos un apartado llamado "getDrugs", que especifica que sirve para
            devolver información sobre el medicamento según el nombre ("Information returned: Drugs related to a specified name" son
            las palabras exactas usadas en la documentación de la API.) Si bajamos un poco, encontramos "drugGroup", dentro del cual
            vemos también "conceptGroup". Dentro de estos dos, tenemos "conceptProperties", que necesitamos para obtener la información,
            así que debemos de asegurarnos de que conceptGroup (que está dentro de "drugGroup", por eso se especifica de esa forma) está
            presente y que no mostremos información que no queremos
            """
            #creamos una donde guardemos la info de los medicamentos en forma de diccionarios (vemos en la API que es un array)
            medicamentos = info_contenida['drugGroup']['conceptGroup']#intenté poder sólo "ConceptGroup" pero como uno estaba dentro del otro, me daba un IndexError
            for med in medicamentos: #vamos a recorrer la lista de medicamentos, sacar la información e imprimirla.
                if 'conceptProperties' in med: #comprobamos que esté "conceptProperties", que si vemos en la documentación no siempre está.
                    for propiedad in med['conceptProperties']: #recorremos todas las propiedades y vamos a seleccionar algunas que podamos imprimir.
                        print(f'Nombre: {propiedad.get("name")}') #con .get, que lo dimos en clase, sacamos un determinado atributo de un diccionario
                        print(f'RXCUI: {propiedad.get("rxcui")}')
                        print(f'TTY: {propiedad.get("tty")}')
                        print(f'Idioma: {propiedad.get("language")}')#he usado comillas dobles porque si no entraba en conflicto con las comillas del f'
                        print('-------------------------------') #un simple separador para que quede más limpio, que al probar el código vi que mareaba
                        print('') #nueva línea

        else: #si no puede acceder al medicamento, elevamos un error.
            raise NameError('El medicamento que has proporcionado no existe o no se encuentra en la base de datos.')

    except requests.exceptions.RequestException as error: #este error ocurre cuando no se puede completar la solicitud con el "https"
        print(f'No se puede completar su solicitud: {error}')

#Aquí para el menú hay que poner solicitar un medicamento.
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Simulación de base de datos en memoria para almacenar los SIPs de los pacientes
sips = {}


def generar_sip(paciente_id: str) -> str:
    '''Genera un SIP único para el paciente.

    Parámetros
    ----------
    paciente_id : str
        Identificador único del paciente para el que se generará el SIP.

    Devuelve
    --------
    str
        SIP generado en formato único 'SIP-<código_hexadecimal>'.
        El código hexadecimal es generado a partir de un UUID, limitado a 10 caracteres y en mayúsculas.

    Ejemplo
    -------
    Si paciente_id es 'P001', el SIP generado podría ser 'SIP-ABC123XYZ'.
    '''
    sip = f'SIP-{uuid.uuid4().hex[:10].upper()}'  # Genera el SIP con uuid version 4, para que el SIP sea único y tenga 10 caracteres
    sips[paciente_id] = sip
    return sip


@app.route('/')
def bienvenida():
    '''Ruta principal que da la bienvenida al sistema y proporciona instrucciones básicas.

    Devuelve
    --------
    jsonify
        Un mensaje de bienvenida con instrucciones sobre cómo usar el sistema.

    Ejemplo
    -------
    { 'mensaje': 'Bienvenido/a al sistema generador de SIPs. Modifica el enlace añadiendo /crear_sip/tu_id_de_paciente para generar tu SIP y usa /consultar_sip/tu_id_de_paciente para consultar el SIP.' }
    '''
    return jsonify({
        'mensaje': 'Bienvenido/a al sistema generador de SIPs. '
                   'Modifica el enlace añadiendo /crear_sip/tu_id_de_paciente para generar tu SIP '
                   'y usa /consultar_sip/tu_id_de_paciente para consultar el SIP.'
    })


@app.route('/crear_sip/<paciente_id>', methods=['GET'])
def crear_sip(paciente_id: str):
    '''Crea un SIP para el paciente especificado por su ID.

    Parámetros
    ----------
    paciente_id : str
        El identificador del paciente para el que se generará el SIP.

    Devuelve
    --------
    jsonify
        Un mensaje confirmando la creación del SIP o informando que el paciente ya tiene uno asignado.

    Ejemplo
    -------
    Si el paciente no tiene un SIP asignado, la respuesta será:
    { 'mensaje': 'SIP creado correctamente', 'sip': 'SIP-ABC123XYZ' }

    Si el paciente ya tiene un SIP asignado, la respuesta será:
    { 'mensaje': 'El paciente ya tiene un SIP asignado', 'sip': 'SIP-ABC123XYZ' }
    '''
    if paciente_id in sips:
        return jsonify({'mensaje': 'El paciente ya tiene un SIP asignado', 'sip': sips[paciente_id]}), 400
    sip = generar_sip(paciente_id)  # Se genera el SIP utilizando la función generar_sip
    return jsonify({'mensaje': 'SIP creado correctamente', 'sip': sip})


@app.route('/consultar_sip/<paciente_id>', methods=['GET'])
def consultar_sip(paciente_id: str):
    '''Consulta el SIP asignado a un paciente por su ID.

    Parámetros
    ----------
    paciente_id : str
        El identificador del paciente cuyo SIP se quiere consultar.

    Devuelve
    --------
    jsonify
        El SIP del paciente si existe, o un mensaje de error si no se encuentra.

    Ejemplo
    -------
    Si el paciente tiene un SIP asignado, la respuesta será:
    { 'paciente_id': 'P001', 'sip': 'SIP-ABC123XYZ' }

    Si no se encuentra un SIP para el paciente, la respuesta será:
    { 'mensaje': 'No se encontró el SIP para ese paciente' }
    '''
    sip = sips.get(paciente_id)  # Recupera el SIP del paciente por su ID
    if sip:
        return jsonify({'paciente_id': paciente_id, 'sip': sip})  # Devuelve el SIP del paciente
    return jsonify(
        {'mensaje': 'No se encontró el SIP para ese paciente'}), 404  # Si no existe el SIP, devuelve un error


if __name__ == '__main__':
    app.run(debug=True)
