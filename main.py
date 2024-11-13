from Clases.classCombate import Combate
from Clases.classPersonaje import Personaje


# Crear personajes con distintos niveles de poder y habilidades
goku = Personaje(nombre="Goku", nivel_de_poder=900, raza="Saiyajin")
goku.agregar_habilidad("Kamehameha")
goku.agregar_habilidad("Kaioken")

vegeta = Personaje(nombre="Vegeta", nivel_de_poder=850, raza="Saiyajin")
vegeta.agregar_habilidad("Final Flash")
vegeta.agregar_habilidad("Galick Gun")

freezer = Personaje(nombre="Freezer", nivel_de_poder=800, raza="Alien")
freezer.agregar_habilidad("Death Beam")

cell = Personaje(nombre="Cell", nivel_de_poder=750, raza="Androide")
cell.agregar_habilidad("Kamehameha")
cell.agregar_habilidad("Death Beam")

piccolo = Personaje(nombre="Piccolo", nivel_de_poder=600, raza="Namekiano")
piccolo.agregar_habilidad("Special Beam Cannon")

# Iniciar combates
print("=== Combate 1: Goku vs Vegeta ===")
combate1 = Combate(goku, vegeta)
combate1.iniciar_combate()

print("\n=== Combate 2: Freezer vs Cell ===")
combate2 = Combate(freezer, cell)
combate2.iniciar_combate()

print("\n=== Combate 3: Piccolo vs Goku ===")
combate3 = Combate(piccolo, goku)
combate3.iniciar_combate()

print("\n=== Combate 4: Vegeta vs Freezer ===")
combate4 = Combate(vegeta, freezer)
combate4.iniciar_combate()

print("\n=== Combate 5: Cell vs Piccolo ===")
combate5 = Combate(cell, piccolo)
combate5.iniciar_combate()
