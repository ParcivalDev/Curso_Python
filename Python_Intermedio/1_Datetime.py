# ------------------------------------
#           FECHAS
# ------------------------------------
# datetime -> fecha y tiempo
# time -> tiempo
# date -> fecha
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

ahoraF = datetime.now().strftime("%d/%m/%Y")  # 05/02/2025
ahora = datetime.now()

print(ahora.month)  # 2
print(datetime.now().hour)  # 20

# Número de segundos desde 1970
timestamp = ahora.timestamp()
print(timestamp)  # 1738784150.449309

# Timestamp a fecha
actual = datetime.fromtimestamp(1738784150.449309)
print(actual)  # 2025-02-05 20:35:50.449309


# Insertar fecha
fechaV1 = datetime.strptime("23/01/1995", "%d/%m/%Y")
fechaV2 = datetime(day=23, month=1, year=1995, minute=34)

print(fechaV1.year)  # 1995
# 34 minutos y 1995 años
print(f"{fechaV2.minute} minutos y {fechaV2.year} años")


# Reutilización
def print_date(fecha):
    dias = ["lunes", "martes", "miércoles",
            "jueves", "viernes", "sábado", "domingo"]
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

    print(f"Hoy es {dias[fecha.weekday()]} día {fecha.day} de {
        meses[fecha.month - 1]} de {fecha.year}")


print_date(fechaV1)  # Hoy es lunes día 23 de enero de 1995

# Funciones relacionadas con el tiempo

tiempo_actual = time(10, 3, 59)
print(tiempo_actual)  # 10:03:59
print(tiempo_actual.minute)  # 3
print(tiempo_actual.min)  # 00:00:00
print(tiempo_actual.max)  # 23:59:59.999999

# tiempo_actual = time(24,63,69)
# print(tiempo_actual) # Error no se puede más de 60 segundos, no se puede más de 60 min y tampoco más de 23 horas ya que las doce son las 00


# Fechas
dias = ["lunes", "martes", "miércoles",
        "jueves", "viernes", "sábado", "domingo"]

fecha = date(1990, 12, 12)
fecha_actual = date.today()
print(fecha_actual.year)  # 2025
print(f"{dias[fecha_actual.weekday()]}")  # viernes


# Operar con fechas
start_timedelta = timedelta(200, 100, 100, weeks=2)
finish_timedelta = timedelta(200, 100, 100, weeks=12)

# Permite restar, sumar y dividir pero no multiplicar
print(finish_timedelta - start_timedelta)  # 70 days, 0:00:00
print(finish_timedelta + start_timedelta)  # 498 days, 0:03:20.000200
print(finish_timedelta / start_timedelta)  # 1.3271010346283223
