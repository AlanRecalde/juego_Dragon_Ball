class MinHeap:
    #Clase para manejar un min-heap manual
    def __init__(self):
        self.heap = []

    def push(self, nodo):
        #Inserta un nodo en el heap
        self.heap.append(nodo)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        #Elimina y devuelve el nodo con la menor prioridad
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()  # Reemplazamos la raíz con el último elemento
        self._sift_down(0)
        return top

    def _sift_up(self, index):
        #Asegura la propiedad del heap al insertar
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index):
        #Asegura la propiedad del heap al eliminar
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

    def is_empty(self):
        #Verifica si el heap está vacío
        return len(self.heap) == 0


def dijkstra_manual_heap(grafo, inicio):
    # Inicializa las distancias a todos los nodos como infinito, excepto el nodo inicial (distancia 0)
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Diccionario para guardar el camino más corto hacia cada nodo
    caminos = {inicio: None}

    # Crea una instancia de MinHeap para manejar los nodos por prioridad (distancia)
    heap = MinHeap()
    heap.push((0, inicio))  # Inserta el nodo inicial con distancia 0

    while not heap.is_empty():
        # Extrae el nodo con la menor distancia actual del heap
        costo_actual, nodo_actual = heap.pop()

        #Si la distancia actual es mayor que la registrada, se omite (ya se procesó un camino más corto)
        if costo_actual > distancias[nodo_actual]:
            continue

        #Itera sobre los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual]:
            #Calcula la nueva distancia acumulada para llegar al vecino
            costo_viaje = costo_actual + peso

            #Si la nueva distancia es menor que la distancia registrada, actualiza
            if costo_viaje < distancias[vecino]:
                distancias[vecino] = costo_viaje
                caminos[vecino] = nodo_actual

                #Inserta el vecino en el heap con la nueva distancia
                heap.push((costo_viaje, vecino))

    # Devuelve las distancias mínimas y los caminos reconstruibles
    return distancias, caminos



# Mapa del universo
mapa = {
    "Tierra": [("Namek", 5), ("Vegeta", 10)],
    "Namek": [("Tierra", 5), ("Kaiosama", 8)],
    "Vegeta": [("Tierra", 10), ("Freezer", 7)],
    "Kaiosama": [("Namek", 8)],
    "Freezer": [("Vegeta", 7)]
}

# Encontrar caminos más cortos desde "Tierra"
distancias, caminos = dijkstra_manual_heap(mapa, "Tierra")

# Mostrar resultados
print("Distancias desde Tierra:", distancias)
