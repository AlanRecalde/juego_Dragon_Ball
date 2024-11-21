#Vamos a usar la bibloteca heapq para la implementacion de la heap binaria  
import heapq

class ColaPrioridadTorneo:
    def __init__(self):
        # decidimos elegir una lista para representar el heap
        self.heap = []

    def agregar_personaje(self, personaje):
        #Agrega un personaje a la cola de prioridades.La prioridad se basa en el nivel de poder.
        #Usamos prioridad negativa para que el heap funcione como un max-heap 
        prioridad = -personaje.nivel_poder
        heapq.heappush(self.heap, (prioridad, personaje))

    def obtener_siguiente_combate(self):
        #Obtiene el siguiente personaje con mayor prioridad para combatir.
        if self.heap:
            _, personaje = heapq.heappop(self.heap)
            return personaje
        else:
            return None

    def esta_vacia(self):
        #este metodo verifica si la cola de prioridades está vacía.
        return len(self.heap) == 0




"""""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def padre(self, i):
        return (i - 1) // 2

    def hijo_izquierdo(self, i):
        return 2 * i + 1

    def hijo_derecho(self, i):
        return 2 * i + 2

    def insertar(self, valor):
        #Agrega un valor al heap y restaura la propiedad de max-heap.
        self.heap.append(valor)  # Agregar al final
        self.heapify_up(len(self.heap) - 1)  # Reubicar hacia arriba

    def extraer_maximo(self):
        #Extrae y devuelve el máximo del heap.
        if not self.heap:
            return None  # El heap está vacío
        
        maximo = self.heap[0]  # El máximo es la raíz
        ultimo = self.heap.pop()  # Elimina el último elemento

        if self.heap:  # Si no está vacío después de la extracción
            self.heap[0] = ultimo  # Mueve el último elemento a la raíz
            self.heapify_down(0)  # Reubica hacia abajo

        return maximo

    def heapify_up(self, i):
        #Reubica el elemento hacia arriba para mantener la propiedad de max-heap.
        while i > 0:
            padre = self.padre(i)
            if self.heap[i] > self.heap[padre]:  # Si el hijo es mayor que el padre
                self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]  # Intercambia
                i = padre  # Continua desde el nuevo índice
            else:
                break

    def heapify_down(self, i):
        #Reubica el elemento hacia abajo para mantener la propiedad de max-heap.
        while True:
            izq = self.hijo_izquierdo(i)
            der = self.hijo_derecho(i)
            mayor = i

            # Compara con el hijo izquierdo
            if izq < len(self.heap) and self.heap[izq] > self.heap[mayor]:
                mayor = izq

            # Compara con el hijo derecho
            if der < len(self.heap) and self.heap[der] > self.heap[mayor]:
                mayor = der

            if mayor == i:  # Si no hay cambios, terminamos
                break

            # Intercambia con el hijo mayor
            self.heap[i], self.heap[mayor] = self.heap[mayor], self.heap[i]
            i = mayor  # Continua desde el nuevo índice

    def mostrar_heap(self):
        #Muestra el heap actual (para depuración).
        print(self.heap)
"""