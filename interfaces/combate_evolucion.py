from random import choice
from random import randint


def interfaz_combate():
    "acciones que se toman durante el combate"
    print("1.golpe")
    print("2.habilidades")
    print("3.transformaciones")
    print("4.cubrirse")


def turno(self):
        """Ejecuta un turno de combate entre los personajes."""
        atacante = self.turno_actual
        defensor = self.personaje2 if atacante == self.personaje1 else self.personaje1
        interfaz_combate()
        opcion=input("¿que accion va a tomar?: ")
        if opcion=="1":
             pass
        elif opcion=="2":
            if atacante.habilidades:
                habilidad = choice(list(atacante.habilidades))
                daño = atacante.calcular_daño(habilidad)  # Usamos el método calcular_daño de la clase Personaje
                defensor.recibir_dano(daño, habilidad)
                print(f"{atacante.nombre} usó {habilidad} en {defensor.nombre} causando {daño} de daño.")
                defensor.mostrar_vida()
            else:
                print(f"{atacante.nombre} no tiene habilidades para atacar.")
                turno()
        elif opcion=="3":
             transformaciones(atacante)
        elif opcion=="4":
             pass
        else:
             print("opcion no valida"),self.turno()
        # Cambiar el turno al otro personaje
        self.turno_actual = defensor

def iniciar_combate(self,combates):
        
        if combates==0:
             return "no quedan mas combates, tu poder actual es de {}".format(self.personaje1.nivel)

        """Inicia el combate hasta que uno de los personajes pierda todos sus puntos de vida."""
        print(f"¡Combate entre {self.personaje1.nombre} y {self.personaje2.nombre} ha comenzado!")

        # Reiniciar vida de ambos personajes antes de comenzar el combate
        self.personaje1.reiniciar_vida()
        self.personaje2.reiniciar_vida()

        poder_base=self.personaje1.nivel
        

        while self.personaje1.esta_vivo() and self.personaje2.esta_vivo():
            self.turno()

        ganador = self.personaje1 if self.personaje1.esta_vivo() else self.personaje2
        print(f"El combate ha terminado. {ganador.nombre} es el ganador.")
        if ganador==self.personaje1: 
          if self.personaje1.nivel==self.personaje2.nivel:
             self.personaje1.nivel=poder_base+randint(100,200)
          
          elif   self.personaje1.nivel>self.personaje2.nivel:
             self.personaje1.nivel=poder_base+randint(25,50)
             
          elif   self.personaje1.nivel==self.personaje2.nivel//2:
             self.personaje1.nivel=poder_base+randint(300,400)
             
          return "tu nivel de poder a aumentado a {} por esta victoria".format(self.personaje1.nivel),iniciar_combate(combates-1)   
        else:
             self.personaje1.nivel=poder_base+randint(5,10)
             return "fuiste derrotado y tu poder solo aumento a {}".format(self.personaje1.poder), iniciar_combate(combates=0)
             
             
def transformaciones(self,atacante):
     if atacante.transformaciones:
        for i in range(len(atacante.transformaciones)):
                transformacions,multi=atacante.transformaciones[i]
                print("{}.{}".format(i+1,transformacions))

        transformacion=int(input("elija una transformacion: "))
        if transformacion>=1 and transformacion<=len(atacante.transformaciones):

          transf,multip=atacante.transformaciones[transformacion-1]
          atacante.nive=atacante.nivel*multip       #se multiplica el poder por la transformacion elegida
            
          del self.transformaciones[transformacion-1]

          return "nivel de poder aumentado a {}".format(atacante.nivel)
        else:
             print("opcion no valida"), self.transformaciones
     else:
          return "no quedan transformaciones", self.turno()
    
                     


    
