from Clases.classCombate import Combate
from interfaces.nivel_interface import INivel
from interfaces.habilidades_interface import IHabilidades

class Personaje(INivel, IHabilidades):
    MAX_NIVEL = 100
    MAX_VIDA = 1000  # Puntos de vida máximos
    MAX_PODER = 1000  # Nivel de poder máximo

    def __init__(self, nombre, nivel_de_poder, raza):
        self.nombre = nombre
        self.nivel_de_poder = nivel_de_poder
        self.raza = raza
        self.habilidades = set()  # Usamos un Set para evitar habilidades repetidas
        self.vida = Personaje.MAX_VIDA
        self.evoluciones = {
            "Normal": 1,
            "Kaioken x2": 2,
            "Kaioken x3": 3,
            "Super Saiyajin": 50,
            "Super Saiyajin 2": 100,
            "Super Saiyajin 3": 400,
            "Super Saiyajin Dios": 800,
            "Super Saiyajin Blue": 1000,
        }
        self.evolucion_actual = "Normal"  # Evolución inicial

    def recibir_dano(self, cantidad, habilidad):
        """Reduce la vida del personaje por la cantidad de daño recibido."""
        self.vida -= cantidad

    def esta_vivo(self):
        return self.vida > 0

    def esta_muerto(self):
        return not self.esta_vivo()
    
    def mostrar_vida(self):
        if self.vida < 0:
            print(f"{self.nombre} murió")
        else:
            print(f"La vida restante de {self.nombre} es: {self.vida}")

    def reiniciar_vida(self):
        """Reinicia la vida del personaje a su máximo."""
        self.vida = Personaje.MAX_VIDA

    def calcular_dano(self, habilidad):
        """Calcula el daño basado en la habilidad y el nivel de poder del personaje."""
        base_dano = {
            "Kamehameha": 0.3,
            "Final Flash": 0.27,
            "Death Beam": 0.285,
            "Special Beam Cannon": 0.21,
        }
        return self.nivel_de_poder * base_dano.get(habilidad, 0.25)

    # Métodos de IHabilidades
    def agregar_habilidad(self, habilidad):
        if habilidad not in self.habilidades:
            self.habilidades.add(habilidad)
            print(f"{self.nombre} ha aprendido la habilidad {habilidad}.")

    # Métodos de INivel
    def subir_nivel(self, incremento=1):
        if self.nivel_de_poder + incremento > Personaje.MAX_NIVEL:
            self.nivel_de_poder = Personaje.MAX_NIVEL
            print("Se alcanzó el nivel máximo.")
        else:
            self.nivel_de_poder += incremento
            print(f"{self.nombre} ha subido al nivel {self.nivel_de_poder}.")

    def evolucionar_poder(self, combates_restantes):
        """Calcula la evolución del nivel de poder tras cada combate usando recursividad y avanza en las evoluciones."""
        if combates_restantes == 0 or self.nivel_de_poder >= Personaje.MAX_PODER:
            return self.nivel_de_poder

        # Obtiene el multiplicador de la evolución actual
        multiplicador = self.evoluciones[self.evolucion_actual]
        nuevo_poder = min(self.nivel_de_poder * multiplicador, Personaje.MAX_PODER)
        print(f"{self.nombre} ha evolucionado a un nivel de poder: {nuevo_poder} con {self.evolucion_actual}")
        self.nivel_de_poder = nuevo_poder

        # Avanza a la siguiente evolución si es posible
        evoluciones_lista = list(self.evoluciones.keys())
        actual_index = evoluciones_lista.index(self.evolucion_actual)
        if actual_index + 1 < len(evoluciones_lista):
            self.evolucion_actual = evoluciones_lista[actual_index + 1]

        # Llama recursivamente con combates decrementados
        return self.evolucionar_poder(combates_restantes - 1)
