from abc import ABC, abstractmethod

class ICombate(ABC):
    @abstractmethod
    def iniciar_combate(self, otro_personaje):
        #Inicia un combate con otro personaje
        pass
