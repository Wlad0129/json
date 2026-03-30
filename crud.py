import json
import os

DATA_JSON = os.path.join('data', 'data.json')

def crear_cliente_json(diccionario):
    registros = leer_cliente_json()
    registros.append(diccionario)
    with open(DATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)

def leer_cliente_json():
    if not os.path.isfile(DATA_JSON):
        return []
    with open(DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def actualizar_cliente_json(id_valor, campo_id, nuevos_datos):
    registros = leer_cliente_json()
    actualizado = False
    for reg in registros:
        if reg[campo_id] == id_valor:
            reg.update(nuevos_datos)
            actualizado = True
    if actualizado:
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
    return actualizado

def eliminar_cliente_json(id_valor, campo_id):
    registros = leer_cliente_json()
    nuevos = [reg for reg in registros if reg[campo_id] != id_valor]
    if len(nuevos) != len(registros):
        with open(DATA_JSON, 'w', encoding='utf-8') as f:
            json.dump(nuevos, f, ensure_ascii=False, indent=2)
        return True
    return False    

def buscar_cliente_id(id_valor, campo_id="id"): 
    registros = leer_cliente_json()
    for reg in registros:
     if reg[campo_id] == id_valor:
        return reg
    return None
    
def buscar_cliente_nombre(nombre):
    registros = leer_cliente_json()
    resultados =[]
    for reg in registros:
        if nombre.lower() in reg["nombre"].lower():
            resultados.append(reg)
    return resultados
    
