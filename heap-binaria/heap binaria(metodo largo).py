

class personaje():
    def __init__(self,personaje,nivel):
        self.nombre=personaje
        self.nivel=nivel

class MaxHeap:
    def __init__(self):
        self.heap=[]

    def swapp(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]

    def burbujeo_arriba(self,index):
        parent=(index-1)//2
        
        if index>0 and self.heap[index].nivel>self.heap[parent].nivel:
            self.swapp(index,parent)
            self.burbujeo_arriba(parent)
        

    def burbujeo_abajo(self,index): #intercambia la raiz con el ultimo valor, luego mueve el valor hasta acomodarlo
        left=2*index+1
        right=2*index+2
        largest=index

        if left < len(self.heap) and self.heap[left].nivel > self.heap[largest].nivel:
            largest = left
        if right < len(self.heap) and self.heap[right].nivel > self.heap[largest].nivel:
            largest = right
        if largest != index:
            self.swapp(index, largest)
            self.burbujeo_abajo(largest)


    def devolver(self): #muestra la heap
        return self.heap

    def insert(self,value): #inserta un personaje al final del arbol,luego lo acomoda
        self.heap.append(value)
        self.burbujeo_arriba(len(self.heap)-1)

    def extract_max(self):  #extrae el personaje con mayor poder
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.burbujeo_abajo(0)
        
        return root

    def obtener_campeones(self):    #comienza el torneo, con sus 3 fases
        if len(self.heap)==8:
            print("fase 1 del combate \n")
            fase1_campeones=[]
            while len(self.heap)>1:
                personaje1=self.extract_max()
                personaje2=self.extract_max()
                ganador=self.combate_torneo(personaje1,personaje2)
                fase1_campeones.append(ganador)

            self.heap=fase1_campeones
            print("fase 2 del combate \n")
            fase2_campeones=[]
            while len(self.heap)>1:
                personaje1=self.extract_max()
                personaje2=self.extract_max()
                ganador=self.combate_torneo(personaje1,personaje2)
                fase2_campeones.append(ganador)
            self.heap=fase2_campeones
            
            print("fase final del combate \n")
            fase_final_campeones=[]
            while len(self.heap)>1:
                personaje1=self.extract_max()
                personaje2=self.extract_max()
                ganador=self.combate_torneo(personaje1,personaje2)
                fase_final_campeones.append(ganador)
            self.heap=fase_final_campeones
            return self.extract_max()
        else:
            return "no hay suficientes personajes, se necesitan 8"
    
    def combate_torneo(self,campeon1,campeon2):
        print(f"¡Combate entre {campeon1.nombre} y {campeon2.nombre} ha comenzado!")

        # Reiniciar vida de ambos personajes antes de comenzar el combate
        
        ganador = campeon1  
        print(f"El combate ha terminado. {ganador.nombre} es el ganador.")
        return ganador
        


personaje1=personaje("Goku",1200)
personaje2=personaje("Gohan",800)
personaje3=personaje("Vegeta",1100)
personaje4=personaje("Trunks",500)
personaje5=personaje("Piccolo",900)
personaje6=personaje("Frezzer",1400)
personaje7=personaje("Broly",1600)
personaje8=personaje("Bardock",1300)



heap=MaxHeap()
heap.insert(personaje1)
heap.insert(personaje2)
heap.insert(personaje3)
heap.insert(personaje4)
heap.insert(personaje5)
heap.insert(personaje6)
heap.insert(personaje7)
heap.insert(personaje8)


campeon=heap.obtener_campeones()
if campeon is not None and type(campeon) is not str:
    print("el ganador del torneo es {}".format(campeon.nombre))
else:
    print (campeon)

        
