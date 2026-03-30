from crud import *

def menu():
    print("\n--- GESTION DE CLIENTES DEL GYM ---")
    print("1. Crear cliente")
    print("2. Leer cliente")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. buscar cliente")
    print("6. salir ")
    print("------------------------------")

def pedir_datos():
    id = int(input("Cedula: "))
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    tipo_plan= input("Ingrese el tipo de plan:")
    status = input("Ingrese estado: ")

    return {"id": id, "nombre": nombre, "edad": edad, "tipo_plan": tipo_plan, "status": status}

if __name__ == "__main__":
    while True:
        menu()
        op = input("Elige una opción: ")
        if op == '1':
            datos = pedir_datos()
            crear_cliente_json(datos)
            print("Registro guardado en JSON.")
        elif op == '2':
             registros = leer_cliente_json()
             print("\nRegistros:")
             for r in registros:
                print(r)
        elif op == '3':
            id_valor = int(input("ID del cliente a actualizar: "))
            nuevos = pedir_datos()
            ok = actualizar_cliente_json(id_valor, 'id', nuevos)
            print("Actualizado." if ok else "No encontrado.")
        elif op == '4':
            id_valor = int(input("ID del cliente a eliminar: "))
            ok = eliminar_cliente_json(id_valor, 'id')
            print("Eliminado." if ok else "No encontrado.")  
        elif op == '5':
            tipo = input("¿buscar por (1) id o (2) nombre?: ")
            if tipo == '1':
                ok = buscar_cliente_id(id_valor, 'id')
            else:
                ok = buscar_cliente_nombre(id_valor, 'nombre')
            print(" " if ok else "No encontrado.")
        elif op == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")