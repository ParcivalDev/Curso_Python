from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO  cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            clientes = []
            for registro in registros:
                cliente = Cliente(
                    registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Error al insertar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido,
                       cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Error al actualizar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.cerrar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)  # Tupla con un solo elemento
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.cerrar_conexion(conexion)


if __name__ == "__main__":
    # Insertar un nuevo cliente
    nuevo_cliente = Cliente(nombre="Paco", apellido="Gonzalez", membresia=400)
    clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
    print(f"Clientes insertados: {clientes_insertados}")

    # Seleccionar todos los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

    # Actualizar un cliente
    cliente_actualizado = Cliente(
        id=3, nombre="Manolo", apellido="Pérez", membresia=500)
    clientes_actualizados = ClienteDAO.actualizar(cliente_actualizado)
    print(f"Clientes actualizados: {clientes_actualizados}")

    # Eliminar un cliente
    cliente_eliminado = Cliente(id=4)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminado)
    print(f"Clientes eliminados: {clientes_eliminados}")

    # Seleccionar todos los clientes después de la actualización
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)
