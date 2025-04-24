from cliente import Cliente
from cliente_dao import ClienteDAO


print("*** ZONA FIT ***")

opcion = None
while opcion != 5:
    print("""Menu:
          1. Listar clientes
          2. Agregar cliente
          3. Modificar cliente
          4. Eliminar cliente
          5. Salir""")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print("\n*** Listado de clientes ***")
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:
        nombre = input("Nombre del cliente: ")
        apellido = input("Apellido del cliente: ")
        membresia = int(input("Número de membresía: "))
        nuevo_cliente = Cliente(
            nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
        print(f"Clientes insertados: {clientes_insertados}")
    elif opcion == 3:
        id_cliente = int(input("ID del cliente a modificar: "))
        nombre = input("Nuevo nombre del cliente: ")
        apellido = input("Nuevo apellido del cliente: ")
        membresia = int(input("Nuevo número de membresía: "))
        cliente_actualizado = Cliente(id_cliente, nombre, apellido, membresia)
        clientes_actualizados = ClienteDAO.actualizar(cliente_actualizado)
        print(f"Clientes actualizados: {clientes_actualizados}")
    elif opcion == 4:
        id_cliente = int(input("ID del cliente a eliminar: "))
        cliente_eliminado = Cliente(id_cliente)
        clientes_eliminados = ClienteDAO.eliminar(cliente_eliminado)
        print(f"Clientes eliminados: {clientes_eliminados}")
    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
