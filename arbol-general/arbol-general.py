class NodoHabilidad:
    def __init__(self, nombre, costo_energia, nivel_requerido):
        self.nombre = nombre
        self.costo_energia = costo_energia
        self.nivel_requerido = nivel_requerido
        self.hijos = []  # Habilidades derivadas

    def agregar_habilidad(self, habilidad):
        """Agrega una habilidad derivada al nodo actual."""
        self.hijos.append(habilidad)

    def __str__(self):
        return f"{self.nombre} (Costo: {self.costo_energia}, Nivel: {self.nivel_requerido})"


class ArbolHabilidades:
    def __init__(self, habilidad_raiz):
        self.raiz = habilidad_raiz

    def agregar_habilidad(self, nombre_padre, nueva_habilidad):
        """
        Agrega una nueva habilidad al árbol como derivada de otra habilidad.
        """
        nodo_padre = self.buscar_habilidad(self.raiz, nombre_padre)
        if nodo_padre:
            nodo_padre.agregar_habilidad(nueva_habilidad)
        else:
            print(f"No se encontró la habilidad {nombre_padre} en el árbol.")

    def buscar_habilidad(self, nodo, nombre):
        """
        Busca un nodo en el árbol por su nombre.
        """
        if nodo.nombre == nombre:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_habilidad(hijo, nombre)
            if resultado:
                return resultado
        return None

    def mostrar_arbol(self, nodo=None, nivel=0):
        """
        Muestra el árbol de habilidades en un formato jerárquico.
        """
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + str(nodo))
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)



# Crear la habilidad raíz
habilidad_raiz = NodoHabilidad("Kamehameha", costo_energia=50, nivel_requerido=5)
arbol = ArbolHabilidades(habilidad_raiz)

# Agregar habilidades derivadas
arbol.agregar_habilidad("Kamehameha", NodoHabilidad("Kamehameha x10", costo_energia=100, nivel_requerido=10))
arbol.agregar_habilidad("Kamehameha x10", NodoHabilidad("Kamehameha x20", costo_energia=200, nivel_requerido=20))
arbol.agregar_habilidad("Kamehameha", NodoHabilidad("Kamehameha Explosivo", costo_energia=120, nivel_requerido=15))

# Mostrar el árbol
print("Árbol de habilidades:")
arbol.mostrar_arbol()

# Buscar una habilidad
habilidad = arbol.buscar_habilidad(arbol.raiz, "Kamehameha x10")
if habilidad:
    print(f"\nHabilidad encontrada: {habilidad}")
else:
    print("\nHabilidad no encontrada.")
