"""
Script para interactuar con la API local (gestión de usuarios y SIPs) y la API RxNorm.

Funcionalidades:
- Obtiene y muestra el menú de opciones según el rol del usuario autenticado.
- Permite interactuar con las opciones específicas del menú de cada rol (paciente, médico, enfermero).
- Permite buscar información de medicamentos usando la API RxNorm.
- Permite crear y consultar SIPs usando la API local.
- Menú con opciones específicas del rol, opciones adicionales (RxNorm, SIPs), y salir.
"""

# === Importaciones ===
import requests

# === Configuración de URLs ===
URL_API = "http://localhost:5000"  # Ajusta este puerto según el puerto de tu API
URL_RXNORM = "https://rxnav.nlm.nih.gov/REST/drugs.json"  # API RxNorm

# === Funciones de Utilidad ===
def param(nombre: str, lon_min: int = 0) -> str:
    """
    Solicita un valor por consola, validando su longitud mínima.

    Parámetros
    ----------
    nombre : str
        Nombre descriptivo del parámetro (p. ej., "Nombre del medicamento").
    lon_min : int, optional
        Longitud mínima permitida para el texto de entrada. Por defecto, 0.

    Devuelve
    -------
    str
        El valor ingresado por el usuario.
    """
    while True:
        entrada = input(f"{nombre} (Longitud mínima: {lon_min}): " if lon_min else f"{nombre}: ")
        if len(entrada) < lon_min:
            print(f"Longitud menor que la requerida: {lon_min}")
        else:
            return entrada

def obtener_informacion_medicamento(medicamento: str) -> None:
    """
    Busca información de un medicamento usando la API RxNorm e imprime los detalles.

    Parámetros
    ----------
    medicamento : str
        Nombre del medicamento del que se desea obtener información.

    Devuelve
    -------
    None
        Imprime la información del medicamento en la consola.
    """
    try:
        response = requests.get(URL_RXNORM, params={'name': medicamento})
        response.raise_for_status()

        data = response.json()

        if 'conceptGroup' in data['drugGroup']:
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
        else:
            print("El medicamento que has proporcionado no existe o no se encuentra en la base de datos.")

    except requests.exceptions.RequestException as error:
        print(f"No se puede completar su solicitud: {error}")

def obtener_menu(username: str, password: str) -> dict:
    """
    Obtiene el menú de opciones desde el endpoint /menu de la API local.

    Parámetros
    ----------
    username : str
        Nombre de usuario para la autenticación básica.
    password : str
        Contraseña para la autenticación básica.

    Devuelve
    -------
    dict
        Diccionario con el rol y el menú de opciones.
    """
    try:
        r = requests.get(f"{URL_API}/menu", auth=(username, password), timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e.response.status_code} - {e.response.text}")
        return {"rol": "", "menu": []}
    except requests.RequestException as e:
        print(f"Error al conectar con la API: {str(e)}")
        return {"rol": "", "menu": []}

# === Función Principal ===
def main() -> None:
    """
    Ejecuta un menú en consola para interactuar con la API local y la API RxNorm.

    Permite interactuar con las opciones específicas del menú según el rol del usuario,
    buscar información de medicamentos, crear/consultar SIPs, y salir.

    Devuelve
    -------
    None
        Esta función no devuelve ningún valor.
    """
    print("Bienvenido al sistema")

    # Solicitar credenciales
    username = param("Nombre de usuario", lon_min=1)
    password = param("Contraseña", lon_min=1)

    # Obtener el menú del usuario
    menu_data = obtener_menu(username, password)
    rol = menu_data.get("rol", "")
    menu = menu_data.get("menu", [])

    if not rol or not menu:
        print("No se pudo obtener el menú. Verifique sus credenciales o el estado del servidor.")
        return

    print(f"\nBienvenido, usuario con rol: {rol}")

    # Determinar la opción de salida según el rol
    opcion_salir = len(menu)  # La última opción del menú es "Salir"

    while True:
        print(f"\n======= MENÚ PARA {rol.upper()} =======")
        for item in menu:
            print(item)
        print("Opciones adicionales:")
        print(f"{opcion_salir + 1}. Buscar información de un medicamento (RxNorm)")
        print(f"{opcion_salir + 2}. Crear SIP para un paciente")
        print(f"{opcion_salir + 3}. Consultar SIP de un paciente")
        print("0. Salir")
        opcion = input("Opción: ")

        # Validar que la opción sea un número válido
        try:
            opcion_num = int(opcion)
            if opcion_num < 0 or opcion_num > opcion_salir + 3:
                print("Opción no válida. Intente de nuevo.")
                continue
        except ValueError:
            print("Opción no válida. Debe ser un número.")
            continue

        # Salir del programa
        if opcion_num == 0:
            print("Saliendo de la aplicación...")
            break

        # Opciones adicionales
        if opcion_num == opcion_salir + 1:  # Buscar información de medicamento (RxNorm)
            medicamento = param("Nombre del medicamento", lon_min=1)
            print(f"\nBuscando información para el medicamento: {medicamento}")
            obtener_informacion_medicamento(medicamento)

        elif opcion_num == opcion_salir + 2:  # Crear SIP para un paciente
            paciente_id = param("ID del paciente", lon_min=1)
            try:
                r = requests.get(f"{URL_API}/crear_sip/{paciente_id}", timeout=5)
                r.raise_for_status()
                print(f"Estado: {r.status_code}")
                print(f"Respuesta: {r.json()}")
            except requests.RequestException as e:
                print(f"Error al crear el SIP: {str(e)}")

        elif opcion_num == opcion_salir + 3:  # Consultar SIP de un paciente
            paciente_id = param("ID del paciente", lon_min=1)
            try:
                r = requests.get(f"{URL_API}/consultar_sip/{paciente_id}", timeout=5)
                r.raise_for_status()
                print(f"Estado: {r.status_code}")
                print(f"Respuesta: {r.json()}")
            except requests.RequestException as e:
                print(f"Error al consultar el SIP: {str(e)}")

        # Opciones específicas del menú según el rol
        elif rol == "paciente":
            match opcion_num:
                case 1:  # Ver información personal
                    try:
                        r = requests.get(f"{URL_API}/pacientes", auth=(username, password), timeout=5)
                        r.raise_for_status()
                        print(f"Estado: {r.status_code}")
                        print(f"Información personal: {r.json()}")
                    except requests.RequestException as e:
                        print(f"Error al ver información personal: {str(e)}")

                case 2:  # Pedir cita (no implementado en la API, placeholder)
                    print("Funcionalidad 'Pedir cita' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /paciente/cita en la API

                case 3:  # Descargar información en PDF
                    try:
                        r = requests.get(f"{URL_API}/paciente/descargar_pdf", auth=(username, password), timeout=5)
                        r.raise_for_status()
                        print(f"Estado: {r.status_code}")
                        print(f"Respuesta: {r.json()}")
                    except requests.RequestException as e:
                        print(f"Error al descargar PDF: {str(e)}")

                case 4:  # Recomendar medicamento según síntomas (no implementado, placeholder)
                    print("Funcionalidad 'Recomendar medicamento' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /paciente/recomendar_medicamento

                case 5:  # Ver citas (no implementado, placeholder)
                    print("Funcionalidad 'Ver citas' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /paciente/citas

                case 6:  # Salir (opción de salida para paciente)
                    print("Saliendo de la aplicación...")
                    return

                case _:
                    print("Opción no válida para el rol paciente.")

        elif rol == "medico":
            match opcion_num:
                case 1:  # Ver lista de pacientes
                    try:
                        r = requests.get(f"{URL_API}/pacientes", auth=(username, password), timeout=5)
                        r.raise_for_status()
                        print(f"Estado: {r.status_code}")
                        print(f"Lista de pacientes: {r.json()}")
                    except requests.RequestException as e:
                        print(f"Error al ver lista de pacientes: {str(e)}")

                case 2:  # Ver citas (no implementado, placeholder)
                    print("Funcionalidad 'Ver citas' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /medico/citas

                case 3:  # Agregar entrada al historial médico (no implementado, placeholder)
                    print("Funcionalidad 'Agregar entrada al historial' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /medico/historial/<id_paciente>

                case 4:  # Salir (opción de salida para médico)
                    print("Saliendo de la aplicación...")
                    return

                case _:
                    print("Opción no válida para el rol médico.")

        elif rol == "enfermero":
            match opcion_num:
                case 1:  # Ver habitaciones asignadas (no implementado, placeholder)
                    print("Funcionalidad 'Ver habitaciones asignadas' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/habitaciones

                case 2:  # Asignar paciente a habitación
                    paciente_id = param("ID del paciente", lon_min=1)
                    numero_habitacion = param("Número de habitación", lon_min=1)
                    try:
                        r = requests.post(
                            f"{URL_API}/pacientes/asignar_habitacion",
                            json={"id_paciente": paciente_id, "numero": numero_habitacion},
                            auth=(username, password),
                            timeout=5
                        )
                        r.raise_for_status()
                        print(f"Estado: {r.status_code}")
                        print(f"Respuesta: {r.json()}")
                    except requests.RequestException as e:
                        print(f"Error al asignar paciente a habitación: {str(e)}")

                case 3:  # Limpiar habitación (no implementado, placeholder)
                    print("Funcionalidad 'Limpiar habitación' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/habitacion/<numero>/limpiar

                case 4:  # Ver pacientes asignados (no implementado, placeholder)
                    print("Funcionalidad 'Ver pacientes asignados' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/pacientes

                case 5:  # Agregar nueva habitación (no implementado, placeholder)
                    print("Funcionalidad 'Agregar nueva habitación' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/habitacion

                case 6:  # Asignar habitación a este enfermero (no implementado, placeholder)
                    print("Funcionalidad 'Asignar habitación a enfermero' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/habitacion/<numero>/asignar_enfermero

                case 7:  # Eliminar paciente de habitación (no implementado, placeholder)
                    print("Funcionalidad 'Eliminar paciente de habitación' no implementada en la API.")
                    # Aquí podrías implementar un endpoint /enfermero/habitacion/<numero>/paciente/<id_paciente>

                case 8:  # Salir (opción de salida para enfermero)
                    print("Saliendo de la aplicación...")
                    return

                case _:
                    print("Opción no válida para el rol enfermero.")

        else:
            print("Rol no reconocido. Saliendo...")
            return

# === Iniciar el Script ===
if __name__ == "__main__":
    main()