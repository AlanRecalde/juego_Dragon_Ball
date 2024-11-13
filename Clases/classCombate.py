from random import choice
from interfaces.combate_interface import ICombate

from random import choice

class Combate(ICombate):
    def __init__(self, personaje1, personaje2):
        self.personaje1 = personaje1
        self.personaje2 = personaje2
        self.turno_actual = personaje1  # Comienza con personaje1

    def turno(self):
        """Ejecuta un turno de combate entre los personajes."""
        atacante = self.turno_actual
        defensor = self.personaje2 if atacante == self.personaje1 else self.personaje1

        if atacante.habilidades:
            habilidad = choice(list(atacante.habilidades))
            dano = atacante.calcular_dano(habilidad)  # Usamos el método calcular_dano de la clase Personaje
            defensor.recibir_dano(dano, habilidad)
            print(f"{atacante.nombre} usó {habilidad} en {defensor.nombre} causando {dano:.2f} de daño.")
            defensor.mostrar_vida()
        else:
            print(f"{atacante.nombre} no tiene habilidades para atacar.")

        # Cambiar el turno al otro personaje
        self.turno_actual = defensor

    def iniciar_combate(self):
        """Inicia el combate hasta que uno de los personajes pierda todos sus puntos de vida."""
        print(f"¡Combate entre {self.personaje1.nombre} y {self.personaje2.nombre} ha comenzado!")

        # Reiniciar vida de ambos personajes antes de comenzar el combate
        self.personaje1.reiniciar_vida()
        self.personaje2.reiniciar_vida()

        while self.personaje1.esta_vivo() and self.personaje2.esta_vivo():
            self.turno()

        ganador = self.personaje1 if self.personaje1.esta_vivo() else self.personaje2
        print(f"El combate ha terminado. {ganador.nombre} es el ganador.")
