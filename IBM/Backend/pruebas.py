

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar_persona(self):
        print(f"Se llama {self.nombre} y su apellido es {self.apellido}")
        
        
nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
persona = Persona(nombre, apellido)
persona.mostrar_persona( )