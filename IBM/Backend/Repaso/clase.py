# Definición de la clase Persona
class Persona:

    contador_persona = 0  # Atributo de clase

    def __init__(self, nombre, dni, edad, apellido="Sin apellido"):
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre  # Atributo público
        self.apellido = apellido  # Atributo público
        self._edad = edad  # Atributo protegido
        self.__dni = dni  # Atributo privado

    def mostrar_persona(self):
        print(
            f"Id: {self.id} Se llama {self.nombre} su apellido es {self.apellido} su dni es {self.__dni} y su edad es {self._edad}")

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("Edad no válida")

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if dni.isalnum() and len(dni) == 9:
            self.__dni = dni
        else:
            print("DNI no válido")

    @staticmethod
    def get_contador_personas_static():
        return Persona.contador_persona

    @classmethod  # Recomendado
    def get_contador_personas_class(cls):
        return cls.contador_persona

# print(Persona.atributo_clase)
# Persona.atributo_clase = "Nuevo atributo de clase"
# print(Persona.atributo_clase)


nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")

persona = Persona(nombre=nombre, apellido=apellido, dni="12345678A", edad=30)
persona.mostrar_persona()

persona2 = Persona(nombre="Jose", dni="87654321B", edad=25)
persona2.mostrar_persona()
persona3 = Persona(nombre="Manuel", dni="531248664L", edad=60)

# Esto no cambia el valor del atributo privado __dni, sino que crea un nuevo atributo público __dni en la instancia persona
persona.__dni = "0000000L"
# Esto cambia el valor del atributo protegido. No se recomienda hacerlo, mejor usar los métodos set_edad y set_dni
persona._edad = 99
persona.mostrar_persona()  # El dni sigue siendo el original


persona.set_edad(35)  # Cambiamos la edad usando el método setter
persona.set_dni("99999999C")  # Cambiamos el dni usando el método setter
persona.mostrar_persona()  # Mostramos la persona con los nuevos valores

print(persona.__dict__)  # Mostramos el diccionario de atributos de la persona
# Resultado: {'id': 1,'nombre': 'Jose', 'apellido': 'Sin apellido', '_edad': 35, '_Persona__dni': '99999999C',  '__dni': '0000000L'}
# OJO: Aquí hay dos atributos diferentes relacionados con el dni:
# - '_Persona__dni': Este es el atributo privado original de la clase, que se accede y modifica correctamente usando los métodos getter y setter.
# - '__dni': Este es un nuevo atributo público que se creó accidentalmente al asignar directamente a persona.__dni.
#   No afecta al atributo privado original y puede causar confusión o errores en el código.
# Por eso es importante usar los métodos setter para modificar atributos privados o protegidos,
# ya que garantizan que los cambios se realicen correctamente y respeten las reglas de validación.

# El contador de personas es: 3
print(
    f"(static) El contador de personas es: {Persona.get_contador_personas_static()}")

print(
    f"(class) El contador de personas es: {Persona.get_contador_personas_class()}")
