#importamos los modulos de las intefaces para poder sobreescribir los metodos 
from interfaces.nivel_interface import INivel
from interfaces.habilidades_interface import IHabilidades

class Personaje(INivel, IHabilidades):
    MAX_NIVEL = 100 #Puntos de nivel máximos
    MAX_VIDA = 1000 #Puntos de vida máximos
    MAX_PODER = 1000 #Nivel de poder máximo

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
            
        }
        self.evolucion_actual = "Normal"  # Evolución inicial

        #Reduce la vida del personaje por la cantidad de daño recibido
    def recibir_dano(self, cantidad, habilidad):
        self.vida -= cantidad
        #metodo que nos retorna si el personaje esta vivo = True; muerto = False
    def esta_vivo(self):
        return self.vida > 0
        #A la inversa, podemos utulizar "return Not" self.esta_vivo() para ahorrarnos volver a escribir codigo y verificar si murio  
    def esta_muerto(self):
        return not self.esta_vivo()
    #Este metodo muestra la vida del personaje, primero validando que no haya muerto
    def mostrar_vida(self):
        if self.vida < 0:
            print(f"{self.nombre} murió")
        else:
            print(f"La vida restante de {self.nombre} es: {self.vida}")

    def reiniciar_vida(self):
        #este metodo reinicia la vida del personaje al maximo
        self.vida = Personaje.MAX_VIDA

    def calcular_dano(self, habilidad):
        #Este metodo calcula el daño basado en la habilidad y el nivel de poder del personaje mediante la multiplicacion del nivel de poder * las habilidades
        base_dano = {
            "Kamehameha": 0.3,
            "Final Flash": 0.27,
            "Death Beam": 0.285,
            "Special Beam Cannon": 0.21,
        }
        return self.nivel_de_poder * base_dano.get(habilidad, 0.25)

    # Sobreescribimos el metodo de la Infterface habilidades_interface, validamos si la habilidad no existe ya en el set, si no esta, la agregamos. (aunque elegimos la estructura de datos SET, la cual no permite elementos duplicados y es redundante valilar si esta en el set, decidimos hacerlo igual para mas controles.) 
    def agregar_habilidad(self, habilidad):
        if habilidad not in self.habilidades:
            self.habilidades.add(habilidad)
            print(f"{self.nombre} ha aprendido la habilidad {habilidad}.")

    #Sobreescribimos el metodo subir_nivel de la interface nivel_interface, validamos que el incremento del nivel no supero el nivel maximo para aumentarlo.
    def subir_nivel(self, incremento=1):
        if self.nivel_de_poder + incremento > Personaje.MAX_NIVEL:
            self.nivel_de_poder = Personaje.MAX_NIVEL
            print("Se alcanzó el nivel máximo.")
        else:
            self.nivel_de_poder += incremento
            print(f"{self.nombre} ha subido al nivel {self.nivel_de_poder}.")