class Personaje():
    def __init__(self,nombre,poder):
        self.nombre=nombre
        self.poder=poder
        self.izquierda=None
        self.derecha=None
    
class Personajes():
    def __init__(self):
        self.raiz=None

    def insertar(self,nombre,poder):
        nuevo_personaje=Personaje(nombre,poder)
        if self.raiz==None:
            self.raiz=nuevo_personaje
        else:
            actual=self.raiz
            while True:
                if poder<actual.poder:
                    if actual.derecha is None:
                        actual.derecha=nuevo_personaje
                        break
                    else:
                        actual=actual.derecha
                elif poder>actual.poder:
                    if actual.izquierda is None:
                        actual.izquierda=nuevo_personaje
                        break
                    else:
                        actual=actual.izquierda

    def mostrar_personajes(self):
        self.mostrar_mas_fuertes(self.raiz)
    
    def mostrar_mas_fuertes(self,personaje):
        if personaje is not None:
            self.mostrar_mas_fuertes(personaje.derecha)
            print("{} con poder {}".format(personaje.nombre,personaje.poder))
            self.mostrar_mas_fuertes(personaje.izquierda)

    def Buscar_personaje(self,poder):
        actual=self.raiz
        while actual is not None:
            if actual.poder == poder:
                return actual
            elif actual.poder>poder:
                actual=actual.derecha
            else: 
                actual=actual.izquierda


pj=Personajes()

pj.insertar("Goku",1800)
pj.insertar("Piccolo",1000)
pj.insertar("Trunks",400)
pj.insertar("Gohan",900)
pj.insertar("Vegeta",1600)
pj.insertar("Broly",2000)
pj.insertar("Bardock",1100)

pj.mostrar_personajes()

personaje=pj.Buscar_personaje(1800)

if personaje:
    print("personaje seleccionado {} con poder {}".format(personaje.nombre,personaje.poder))