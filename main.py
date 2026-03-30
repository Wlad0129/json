"""
Módulo Principal de Interacción (Interfaz de Consola).
Permite navegar por el menú, ingresar datos y comunicarse con las operaciones CRUD.
"""
from crud import *

def menu():
    """Imprime las opciones del sistema en consola."""
    print("\n" + "="*45)
    print(" SISTEMA DE GESTIÓN DE CLIENTES DEL GIMNASIO")
    print("="*45)
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")
    print("-" * 45)

def pedir_entero(mensaje):
    """
    Función helper de validación y control de flujo con try/except.
    Asegura que el usuario solo pueda ingresar un número entero válido.
    Cumple con el Criterio 5 (Manejo de Errores - try/except).
    """
    while True:
        valor = input(mensaje)
        try:
            # Intentamos convertir la entrada a número entero
            entero = int(valor)
            if entero < 0:
                print("=> Error: El número no puede ser negativo.")
                continue
            return entero
        except ValueError:
            # Capturamos el error de tipo ValueError si meten texto o símbolos
            print("=> Error: Dato inválido. Debes ingresar un número entero válido.")

def pedir_datos(id_proporcionado=None):
    """
    Solicita y valida la información de un nuevo cliente.
    Si recibe `id_proporcionado`, usa ese, si no, lo pide.
    Asegura integridad de datos y evita errores (Manejo de errores requeridos).
    """
    if id_proporcionado is None:
        while True:
            id_cliente = pedir_entero("Ingrese la Cédula/ID único: ")
            
            # Verificamos si el ID ya existe antes de crearlo (Validación Criterio 5)
            if buscar_cliente_id(id_cliente) is not None:
                print("=> Error: Ya existe un cliente con ese ID. Intenta ingresarlo de nuevo.")
            else:
                break
    else:
        id_cliente = id_proporcionado

    # Bucle para asegurar que no nos dejen el nombre vacio
    while True:
        nombre = input("Ingrese el Nombre: ").strip()
        if nombre:
            break
        print("=> Error: El nombre no puede estar vacío.")

    edad = pedir_entero("Ingrese la Edad: ")
    
    # Manejo de opciones cerradas para el tipo de plan
    while True:
        op_plan = input("Ingrese el tipo de plan (1. mensual, 2. trimestral, 3. anual): ")
        if op_plan == '1':
            tipo_plan = "mensual"
            break
        elif op_plan == '2':
            tipo_plan = "trimestral"
            break
        elif op_plan == '3':
            tipo_plan = "anual"
            break
        else:
            print("=> Error: Opción inválida. Intente de nuevo.")

    # Manejo de opciones cerradas para el estado
    while True:
        op_status = input("Ingrese estado (1. activo, 2. inactivo): ")
        if op_status == '1':
            status = "activo"
            break
        elif op_status == '2':
            status = "inactivo"
            break
        else:
            print("=> Error: Opción inválida. Intente de nuevo.")

    # Guardamos organizadamente en un diccionario (Criterio 2: Diccionarios)
    return {
        "id": id_cliente,
        "nombre": nombre,
        "edad": edad,
        "tipo_plan": tipo_plan,
        "status": status
    }

def imprimir_cliente(cliente):
    """Manejo de visualización atractiva de un diccionario cliente (Criterio 6: Código Limpio)."""
    # Imprime algo simple, legible y estético. 
    print(f"[{cliente['id']}] {cliente['nombre']} | {cliente['edad']} años | Plan: {cliente['tipo_plan'].capitalize()} | Estado: {cliente['status'].capitalize()}")

def iniciar_sistema():
    """Función principal del menú interactivo de la aplicación."""
    while True:
        menu()
        op = input("Elige una opción (1-6): ")
        
        # 1. Crear cliente
        if op == '1':
            print("\n--- NUEVO CLIENTE ---")
            datos_nuevo = pedir_datos() # Pide los datos con sus validaciones
            crear_cliente_json(datos_nuevo)
            print("\n=> ¡Cliente guardado exitosamente!")
            
        # 2. Listar clientes
        elif op == '2':
            print("\n--- LISTA DE CLIENTES ---")
            registros = leer_cliente_json()
            if not registros:
                print("=> No hay clientes registrados aún en el sistema.")
            else:
                for r in registros:
                    imprimir_cliente(r)
                    
        # 3. Buscar cliente
        elif op == '3':
            print("\n--- BUSCAR CLIENTE ---")
            # Bucle while para la elección de búsqueda (Criterio 4)
            while True:
                tipo = input("¿Buscar por (1) ID o (2) Nombre?: ")
                if tipo in ['1', '2']:
                    break
                print("=> Error: Opción inválida de búsqueda.")
                
            if tipo == '1':
                id_buscar = pedir_entero("Ingrese el ID a buscar: ")
                resultado = buscar_cliente_id(id_buscar)
                if resultado:
                    print("\nRegistro encontrado:")
                    imprimir_cliente(resultado)
                else:
                    print("=> Cliente no encontrado con ese ID.")
                    
            elif tipo == '2':
                nombre_buscar = input("Ingrese el nombre parcial o completo a buscar: ").strip()
                resultados = buscar_cliente_nombre(nombre_buscar)
                if resultados:
                    print(f"\nSe encontraron {len(resultados)} registro(s):")
                    for r in resultados:
                        imprimir_cliente(r)
                else:
                    print("=> No se encontraron clientes con ese nombre.")
                
        # 4. Actualizar cliente
        elif op == '4':
            print("\n--- ACTUALIZAR CLIENTE ---")
            # Usamos nuestra validación robusta (helper pedir_entero)
            id_valor = pedir_entero("Ingrese el ID del cliente a actualizar: ")
            
            if buscar_cliente_id(id_valor) is not None:
                # Si existe, le pedimos nuevos datos, forzando usar el mismo ID
                print(f"Ingresando nuevos datos para el ID: {id_valor}")
                nuevos_datos = pedir_datos(id_proporcionado=id_valor)
                actualizado = actualizar_cliente_json(id_valor, 'id', nuevos_datos)
                if actualizado:
                    print("\n=> ¡Los datos del cliente fueron actualizados correctamente!")
                else:
                    print("\n=> Error interno en actualización.")
            else:
                print("=> Error: No se encontró un cliente con este ID para actualizar.")
                
        # 5. Eliminar cliente
        elif op == '5':
            print("\n--- ELIMINAR CLIENTE ---")
            id_valor = pedir_entero("Ingrese el ID del cliente a eliminar: ")
            
            # Pedir confirmación antes de borrar
            if buscar_cliente_id(id_valor) is not None:
                while True:
                    seguro = input(f"¿Estás seguro que deseas eliminar el ID {id_valor}? (s/n): ").lower()
                    if seguro in ['s', 'n']:
                        break
                    
                if seguro == 's':
                    eliminado = eliminar_cliente_json(id_valor, 'id')
                    if eliminado:
                        print("\n=> ¡Cliente eliminado del sistema!")
                    else:
                        print("\n=> Hubo un error al eliminar.")
                else:
                    print("\n=> Operación cancelada.")
            else:
                 print("=> Error: No se encontró un cliente con este ID para eliminar.")
                 
        # 6. Salir
        elif op == '6':
            print("\n¡Gracias por utilizar el sistema de gestión del Gimnasio!")
            break
            
        else:
            print("\n=> Error: Por favor, ingrese un número de opción válido (1-6).")

if __name__ == "__main__":
    iniciar_sistema()