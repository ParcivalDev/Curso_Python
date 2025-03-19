def dias(dia):
    match dia:
        case "Lunes":
            return "Hoy es Lunes, empieza la semana."
        case "Martes":
            return "Hoy es Martes, seguimos con la semana."
        case "Miércoles":
            return "Hoy es Miércoles, estamos a mitad de semana."
        case "Jueves":
            return "Hoy es Jueves, casi fin de semana."
        case "Viernes":
            return "Hoy es Viernes, último día laboral para muchos."
        case "Sábado":
            return "Hoy es Sábado, disfruta tu fin de semana."
        case "Domingo":
            return "Hoy es Domingo, aprovecha para descansar."
        case _:
            return "Ese no es un día válido."

dia = input("¿Qué día de la semana es hoy? ")
print(dias(dia))
