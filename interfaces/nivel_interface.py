from abc import ABC, abstractmethod

class INivel(ABC):
    @abstractmethod
    def subir_nivel(self, incremento):
        #Sube el nivel de un personaje
        pass
