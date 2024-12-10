from humain import Humain 

class Barman(Humain):
    def __init__(self, name, name_bar=None, fin_phrase="CoCo"):
        super().__init__(name, drink="Vin")
        self.name_bar = name_bar

        if name_bar is None:
            self.name_bar = f"Chez {self.quelEstTonNom()}"
        else:
            self.name_bar = name_bar
        
        self.fin_phrase = fin_phrase

    def manger(self):
        return f"{self.quelEstTonNom()} mange un steak avec des pommes de terre !{self.fin_phrase}"

    def presentation(self):
        return f"Bonjour, je suis {self.quelEstTonNom()}, et je vous presente mon bar de {self.name_bar}.\n"

    