print("Clases V2 Eliseo Nava")
#Zona de clase
class Datos:
    #El constructor
    def __init__(self, estatura,peso):
        self.estatura=estatura
        self.peso=peso 
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} Kg")
    def mi_lista(self):
        Carros=["Chevrolet Camaro 4 Cilindros Turbo 2017 Color Azul Rey","Dodge Challenger SRT Scat Pack","Ford Mustang Boss 302"]
        print(Carros)
        for carritos in Carros:
            print(carritos)
    def mi_tupla(self):
        Frutas=("Lechuga","Tomate","Espinaca")
        print(Frutas)
        for fruit in Frutas:
            print(fruit)
    def mi_set(self):
        Animales={"Hamster","Huron","Gato"}
        print(Animales)
        for Animal in Animales:
            print(Animal)
    def mi_dic(self):
        Diccionario = {
            "Marca:": "Chevrolet",
            "Modelo:": "Camaro",
            "Año:": 2017,
            "Color:": "Azul Rey"
            }
        for dick, di in Diccionario.items():
            print(dick,di)

#creacion de objeto info
info=Datos(1.75,70)

#utilizando el obj.
info.mostrar_datos()
print("Lista de mis carritos")
info.mi_lista()
print("Tupla de Verduras")
info.mi_tupla()
print("Sets de animales")
info.mi_set()
print("Diccionario de un camaro")
info.mi_dic()