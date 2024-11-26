class Ruta_planetas:
    def __init__(self): #diccionario en donde guardar las rutas
        self.ruta={}

    def agregar_planeta(self,planeta):  #se agrega el nodo planeta
        if planeta not in self.ruta:
            self.ruta[planeta]=[]

    def agrar_ruta(self,planeta1,planeta2): #se agregan conexiones entre 2 planetas
        if planeta1 in self.ruta and planeta2 in self.ruta:
            self.ruta[planeta1].append(planeta2)
            self.ruta[planeta2].append(planeta1)

    def mapa(self):     #mapa del universo
        for ruta in self.ruta:
            print(f"{ruta}:{self.ruta[ruta]}")

    def viaje(self,origen,destino): #metodo para viajar
        
        if origen in self.ruta and destino in self.ruta[origen]:
            print("viajando desde {} hasta {}".format(origen,destino))
        else:
            print("no es posible viajar hacia {} desde este punto".format(destino))

    def mostrar_rutas(self,planeta):    #muestra las rutas del planeta seleccionado u origen
        if planeta in self.ruta:
            print("rutas del planeta {}:{}".format(planeta,self.ruta[planeta]))

    def camino_mas_rapido(self, inicio, destino):
        
        # Cola que almacenará los planetas y sus caminos
        cola = [(inicio, [inicio])]  # Tupla (planeta, camino)
        
        # Lista para almacenar los planetas visitados (simulando un conjunto)
        visitados = []
        
        while cola:
            planeta_actual, camino = cola.pop(0)  # Extraemos el primer elemento de la cola
            
            if planeta_actual == destino:
                return camino  # Si llegamos al destino, devolvemos el camino recorrido
            
            if planeta_actual not in visitados:
                visitados.append(planeta_actual)  # Marcamos el planeta como visitado

                # Añadimos los planetas adyacentes a la cola
                for vecino in self.ruta.get(planeta_actual, []):
                    if vecino not in visitados:
                        cola.append((vecino, camino + [vecino]))
        


planeta=Ruta_planetas()
planeta.agregar_planeta("Tierra")
planeta.agregar_planeta("Vegeta")
planeta.agregar_planeta("Namek")
planeta.agregar_planeta("Planeta Sagrado")
planeta.agregar_planeta("Planeta Kaio")
planeta.agregar_planeta("Sadala")

planeta.agrar_ruta("Tierra","Namek")
planeta.agrar_ruta("Tierra","Vegeta")
planeta.agrar_ruta("Tierra","Sadala")
planeta.agrar_ruta("Namek","Vegeta")
planeta.agrar_ruta("Namek","Planeta Sagrado")
planeta.agrar_ruta("Vegeta","Sadala")
planeta.agrar_ruta("Planeta Kaio","Planeta Sagrado")

print("Mapa del universo \n")
planeta.mapa()

print("")

planeta.mostrar_rutas("Tierra")

print("")

planeta.viaje("Tierra","Vegeta")
print("")
planeta.viaje("Tierra","Planeta Sagrado")
print("")

camino=planeta.camino_mas_rapido("Tierra","Planeta Kaio")

print("el camino mas rapido para llegar al destino es={}".format(camino))

