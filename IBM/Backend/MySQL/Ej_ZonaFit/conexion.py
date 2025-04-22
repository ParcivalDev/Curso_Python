from mysql.connector import Error
from mysql.connector import pooling

# Clase que gestiona la conexión a la base de datos mediante un pool
class Conexion:
    # Configuración de conexión (constantes de clase)
    DATABASE = "zona_fit_db"
    USERNAME = "root"
    PASSWORD = "1234"
    DB_PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"

    # Variable que almacenará el pool de conexiones (a nivel de clase)
    pool = None

    # Método de clase porque accede/modifica variables de clase (como cls.pool)
    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                # Creamos el pool solo si no ha sido creado antes
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Error: {e}")
        else:
            # Si el pool ya existe, lo devolvemos directamente
            return cls.pool

    # También es de clase porque llama a otro método de clase y podría reutilizar el pool de clase
    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        if pool:
            return pool.get_connection()
        else:
            print("No se pudo obtener el pool de conexiones.")
            return None

    # Método estático porque no accede ni a la clase ni a una instancia: solo cierra la conexión
    @staticmethod
    def cerrar_conexion(conexion):
        conexion.close()


# Esto se ejecuta solo si el archivo se corre directamente (no si se importa desde otro script)
if __name__ == '__main__':
    pool = Conexion.obtener_pool()  # Obtenemos el pool
    print(pool)

    conexion = Conexion.obtener_conexion()  # Obtenemos una conexión desde el pool
    if conexion:
        print("Conexión obtenida correctamente.")
        Conexion.cerrar_conexion(conexion)  # Cerramos la conexión
    else:
        print("No se pudo obtener una conexión.")
