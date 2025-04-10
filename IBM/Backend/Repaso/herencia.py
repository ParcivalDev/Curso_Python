

class Animal:
    def comer(self):
        print("Comiendo")
    
    def dormir(self):
        print("ZzZzZzZz")
    
    


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")
        
        
perro = Perro()

perro.comer()
perro.dormir()
perro.hacer_sonido()