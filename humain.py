from abc import ABC, abstractmethod

class Humain(ABC):
    def __init__(self, name, drink):
        self.__name = name
        self.__drink = drink     

    def quelEstTonNom(self):
        return self.__name

    def quelEstTaBoisson(self):
        return self.__drink
    
    def sepresenter(self):
        return f"Bonjour, je suis {self.__name} et j'aime le {self.__drink}.\n"
    
    @abstractmethod
    def manger(self):
        pass

