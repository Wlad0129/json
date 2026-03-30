"""
Módulo CRUD (Create, Read, Update, Delete) para la gestión
de clientes del gimnasio. Utiliza un archivo JSON como persistencia de datos.
"""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(BASE_DIR, 'data', 'data.json')
os.makedirs(os.path.dirname(DATA_JSON), exist_ok=True)

def crear_cliente_json(diccionario):
    """
    Agrega un nuevo cliente a la lista de registros y guarda el archivo.
    Recibe un diccionario con los datos del cliente.
    """
    registros = leer_cliente_json()
    registros.append(diccionario)
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

def leer_cliente_json():
    """
    Carga todos los clientes almacenados en el archivo JSON.
    Retorna una lista de diccionarios. Si no existe el archivo, retorna lista vacía.
    """
    if not os.path.isfile(DATA_JSON):
        return []
    with open(DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def actualizar_cliente_json(id_valor, campo_id, nuevos_datos):
    """
    Actualiza la información de un cliente específico basado en su ID.
    Retorna True si fue actualizado con éxito, False si no se encontró.
    """
    registros = leer_cliente_json()
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)
            actualizado = True
            break
            
    if actualizado:
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
            
    return actualizado

def eliminar_cliente_json(id_valor, campo_id):
    """
    Elimina a un cliente de los registros basado en su ID.
    Retorna True si fue eliminado, False si el ID no existía.
    """
    registros = leer_cliente_json()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]
    
    if len(nuevos) != len(registros):
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(nuevos, f, ensure_ascii=False, indent=2)
        return True
        
    return False    

def buscar_cliente_id(id_valor, campo_id="id"): 
    """
    Busca a un cliente específico por su ID.
    Retorna el diccionario con sus datos si lo encuentra, de lo contrario None.
    """
    registros = leer_cliente_json()
    for reg in registros:
        if reg[campo_id] == id_valor:
            return reg
    return None
    
def buscar_cliente_nombre(nombre):
    """
    Busca clientes cuyo nombre contenga el parámetro ingresado (búsqueda parcial).
    Retorna una lista con los registros coincidentes.
    """
    registros = leer_cliente_json()
    resultados = []
    for reg in registros:
        if nombre.lower() in reg["nombre"].lower():
            resultados.append(reg)
    return resultados
