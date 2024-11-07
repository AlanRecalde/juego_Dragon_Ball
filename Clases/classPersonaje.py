from interfaces.combate_interface import ICombate
from interfaces.nivel_interface import INivel
from interfaces.habilidades_interface import IHabilidades



class Personaje(ICombate, INivel, IHabilidades):
    MAX_NIVEL = 100  # Nivel máximo permitido

    def __init__(self, nombre, nivel_de_poder, raza):
        self.nombre = nombre
        self.nivel_de_poder = nivel_de_poder
        self.raza = raza
        self.habilidades = set()  # Usamos un conjunto para evitar habilidades duplicadas

    # Implementación de INivel
    def subir_nivel(self, incremento=1):
        """Aumenta el nivel de poder del personaje sin exceder el límite máximo."""
        try:
            if self.nivel_de_poder + incremento > Personaje.MAX_NIVEL:
                self.nivel_de_poder = Personaje.MAX_NIVEL
                raise ValueError("Se alcanzó el nivel máximo para el personaje.")
            self.nivel_de_poder += incremento
            print(f"{self.nombre} ha subido al nivel de poder {self.nivel_de_poder}.")
        except ValueError as e:
            print(e)

    # Implementación de IHabilidades
    def agregar_habilidad(self, habilidad):
        """Agrega una nueva habilidad al personaje si no la tiene ya."""
        try:
            if habilidad in self.habilidades:
                raise ValueError(f"{self.nombre} ya posee la habilidad {habilidad}.")
            self.habilidades.add(habilidad)
            print(f"{self.nombre} ha aprendido la habilidad {habilidad}.")
        except ValueError as e:
            print(e)

    # Implementación de ICombate
    def iniciar_combate(self, otro_personaje):
        """Inicia un combate con otro personaje."""
        print(f"{self.nombre} ha iniciado un combate con {otro_personaje.nombre}.")






# Crear personajes de Dragon Ball
goku = Personaje(nombre="Goku", nivel_de_poder=5000, raza="Saiyajin")
vegeta = Personaje(nombre="Vegeta", nivel_de_poder=4800, raza="Saiyajin")
piccolo = Personaje(nombre="Piccolo", nivel_de_poder=3500, raza="Namekuseijin")
krillin = Personaje(nombre="Krillin", nivel_de_poder=1000, raza="Terrícola")

# Agregar habilidades a cada personaje
goku.agregar_habilidad("Kamehameha")
goku.agregar_habilidad("Kaioken")
vegeta.agregar_habilidad("Galick Gun")
piccolo.agregar_habilidad("Makankosappo")
krillin.agregar_habilidad("Destructo Disc")

# Subir nivel de poder a personajes antes del combate
goku.subir_nivel(500)
vegeta.subir_nivel(300)
krillin.subir_nivel(1200)  # Subiendo a su límite

# Prueba de combate
print("\n--- Inicio de Combates ---")
goku.iniciar_combate(vegeta)    # Combate entre Goku y Vegeta
vegeta.iniciar_combate(piccolo)  # Combate entre Vegeta y Piccolo
piccolo.iniciar_combate(krillin) # Combate entre Piccolo y Krillin

