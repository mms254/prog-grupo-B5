"""
Estas funciones pretenden servir para la recomendación de medicamentos a pacientes sin tener que tomar cita con un médico previamente.
Debemos importar las clases Paciente y Medicamento para poder comprobar correctamente la compatibilidad.
"""
from typing import Union
from medicamento import Medicamento
from paciente import Paciente

def recomendar_medicamento(paciente:Paciente , lista_medicamentos:list) -> list:
    """
    Devuelve una lista con los medicamentos que puede tomar el paciente, teniendo en cuenta los síntomas y las alergias.

    Parámetros:
    -----------
    paciente: objeto Paciente
        El paciente que debe tomar el medicamento.
    lista_medicamentos: list
        Lista con los objetos medicamentos.

    Devuelve:
    ---------
    medicamentos_adecuados: list
        Una lista de los medicamentos que podría tomarse el paciente. Siempre es importante que lea las instrucciones de dicho
        medicamento y consulte a su farmacéutico.
    medicamentos_filtrados: list
        Una lista con los medicamentos filtrados según la contención de alérgenos que afecten al paciente
    """
    sintomas_paciente = [] #Creamos esta lista para almacenar los síntomas que tiene un paciente
    for enfermedad in paciente.enfermedades: #recorremos las enfermedades
        sintomas_paciente.extend(enfermedad.sintomas) #y añadimos con extend los síntomas que tienen.


    medicamentos_adecuados = [] #Creamos una lista vacía donde iremos añadiendo los medicamentos que puede tomar un paciente.


    if sintomas_paciente: #necesitamos que tenga síntomas el paciente, si no, no lo podemos curar
        for medicamento in lista_medicamentos: #creamos un bucle para recorrer la lista de los medicamentos que disponemos en nuestra base de datos
            for sintoma in sintomas_paciente: #bucle que recorre la lista de síntomas que tiene un paciente
                if sintoma in medicamento.sintomas_curables: #en caso de que el medicamento cure dicho síntoma...
                    medicamentos_adecuados.append(medicamento) #añadimos el medicamento a nuestra lista de medicamentos adecuados
                    break #rompemos el bucle, porque si un medicamento cura más de un síntoma, se añadirá múltiples veces a la lista

        if paciente.alergias: #comprobamos si el paciente tiene o no alergias
            medicamentos_filtrados = [] #hacemos una lista vacía donde filtraremos los medicamentos con alérgenos
            for medicamento in medicamentos_adecuados: #hora recorremos la lista de medicamentos adecuados que hemos creado antes
                tiene_alergenos = False  # creamos un "flag" sobre la contención de alergenos
                for alergia in paciente.alergias: #y también recorremos la lista de alergias que tienen los pacientes.
                    if alergia in medicamento.alergenos: #si el medicamento adecuado que comprobamos actualmente contiene un alérgeno peligroso para el paciente...
                        tiene_alergenos = True #cambiamos tiene_alergenos a True.
                        break #rompemos el bucle en cuanto encontramos que tiene un alérgeno
                if not tiene_alergenos:
                    medicamentos_filtrados.append(medicamento) #filtramos los medicamentos.
                    #Es mejor hacer una lista nueva que eliminarlos, porque puede causar problemas
            return medicamentos_filtrados

        else: #si no tiene alergia, devolvemos la lista original
            return medicamentos_adecuados


    else: #en caso de que el paciente esté sano, devolvemos un error
        raise ValueError('El paciente no tiene síntomas')

def comprobacion_alergenos(paciente:Paciente, medicamentos:Union[list,Medicamento]) -> Union[dict, str]:
    """
    Esta función sirve para comprobar de manera más sencilla si unos medicamentos que le han sido recetados a nuestro paciente
    (ya sea en nuestro centro ProSalud o en otro centro clínico ajeno) contienen alérgenos que afecten al paciente, con el objetivo de evitar
    una posible reacción alérgica o incluso un choque anafiláctico (muerte debido a una reacción alérgica intensa)

    Parámetros:
    ------------
    paciente: objeto Paciente
        El paciente que debe tomar el medicamento.
    medicamentos: Union[list,Medicamento]
        Lista con los objetos medicamentos que le han recetado y/o recomendado al paciente, o un str en caso de que sea sólo un medicamento.

    Devuelve:
    ---------
    comprobacion_alergenos: dict
        Un diccionario cuyas claves son los nombres de los medicamentos recetados y cuyo valor correspondiente es 'Seguro' o 'Contiene alérgenos'
        según si el paciente puede o no tomarlo.

    """

    comprobar_alergenos = {} #diccionario vacío para poder comprobar la seguridad de los medicamentos.
    if paciente.alergias: #si el paciente tiene alergias
        if isinstance(medicamentos, Medicamento): #primero comprobamos si nos han dado el medicamento como objeto de la clase Medicamento
            for alergia in paciente.alergias: #recorremos la lista de alergias:
                if alergia in medicamentos.alergenos: #si el medicamento contiene algún alérgeno peligroso
                    comprobar_alergenos[medicamentos.nombre] = 'Contiene alérgenos' #actualizamos el diccionario.
                    break #rompemos el bucle: con que tenga un alérgeno ya no podemos arriesgar a ofrecérselo a un paciente.
                else: #en caso de que no contenga alérgenos:
                    comprobar_alergenos[medicamentos.nombre] = 'Seguro' #marcamos el medicamento como seguro.
                    #Si al continuar con el bucle se encuentra algún alérgeno, se sobreescribe.
        elif isinstance(medicamentos, list):
            for medicamento in medicamentos:
                es_seguro = True #iniciamos a True, si no es seguro lo cambiaremos.
                for alergia in paciente.alergias:
                    if alergia in medicamento.alergenos:
                        comprobar_alergenos[medicamento.nombre] = 'Contiene alérgenos'
                        es_seguro = False
                        break
                if es_seguro: #una vez sabemos que es seguro, lo marcamos como tal
                    comprobar_alergenos[medicamento.nombre] = 'Seguro'
        return comprobar_alergenos
    else:
        raise ValueError('El paciente no tiene alergias')