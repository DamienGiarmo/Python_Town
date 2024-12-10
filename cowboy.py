from humain import Humain

class Cowboy(Humain):
    def __init__(self, name, adjectif="intrépide", popularité=0):
        super().__init__(name, drink="Whisky")
        self.adjectif = adjectif
        self.popularité = popularité

    def manger(self):
        return f"{self.quelEstTonNom()} mange un steak avec des pommes de terre !"

    def delivrer(self, dame):
        if dame.etat:
            dame.libérer(self)
            self.popularité += 1
            return f"{self.quelEstTonNom()} a délivré {dame.quelEstTonNom()}! Sa popularité est maintenant de {self.popularité}."
        return f"{dame.quelEstTonNom()} est déjà libre!"

    def tirer(self, brigand):
        return f"Le {self.quelEstTonNom()} {self.adjectif} tire sur {brigand.quelEstTonNom()}. PAN PAN !!!\n"

    def presentation(self):
        base_presentation = super().sepresenter() 
        specific_presentation = (
            f"On m'appelle {self.quelEstTonNom()} {self.adjectif} !!!\n"
            f"Ma popularité est de {self.popularité} !"
        )
        return f"{base_presentation}\n{specific_presentation}\n"
