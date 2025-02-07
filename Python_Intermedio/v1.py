# # ------------------------------------
# #           FECHAS
# # ------------------------------------
from datetime import datetime

# ahoraF = datetime.now().strftime("%d/%m/%Y")  # 05/02/2025
# ahora = datetime.now()

# print(ahora.month)  # 2
# print(datetime.now().hour)  # 20

# # Número de segundos desde 1970
# timestamp = ahora.timestamp()
# print(timestamp)  # 1738784150.449309

# # Timestamp a fecha
# actual = datetime.fromtimestamp(1738784150.449309)
# print(actual)  # 2025-02-05 20:35:50.449309


# # Insertar fecha
# fechaV1 = datetime.strptime("23/01/1995", "%d/%m/%Y")
# fechaV2 = datetime(day=23, month=1, year=1995, minute=34)

# print(fechaV1.year)  # 1995
# # 34 minutos y 1995 años
# print(f"{fechaV2.minute} minutos y {fechaV2.year} años")


# # Reutilización
# def print_date(fecha):
#     dias = ["lunes", "martes", "miércoles",
#             "jueves", "viernes", "sábado", "domingo"]
#     meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
#              "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

#     print(f"Hoy es {dias[fecha.weekday()]} día {fecha.day} de {
#         meses[fecha.month - 1]} de {fecha.year}")


# print_date(fechaV1)  # Hoy es lunes día 23 de enero de 1995

