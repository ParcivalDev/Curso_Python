

class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("ZzZzZzZz")

    def __str__(self):
        return f"Animal: {super.__str__(self)}"


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau") 

    def dormir(self):
        print("Perro: ZzZzZzZzZ")


perro = Perro()

perro.comer()
perro.dormir()  # Perro: ZzZzZzZzZ
perro.hacer_sonido()

print(perro.__str__())
