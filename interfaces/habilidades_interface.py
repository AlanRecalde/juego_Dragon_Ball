from abc import ABC, abstractmethod

class IHabilidades(ABC):
    @abstractmethod
    def agregar_habilidad(self, habilidad):
        #Agrega una nueva habilidad al personaje
        pass
