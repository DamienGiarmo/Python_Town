from cowboy import Cowboy

class Sherif(Cowboy):
    def __init__(self, name, popularité=0, brigand_coffres=10):
        super().__init__(name, adjectif="honnête", popularité=popularité)
        self.brigand_coffres = brigand_coffres

    def coffrer(self, brigand):
        if not brigand.en_prison:
            brigand.en_prison = True
            self.brigand_coffres += 1
            return f"Au nom de la loi, je vous arrête, {brigand.quelEstTonNom()} !\n"
        return f"{brigand.quelEstTonNom()} est déjà en prison !"

    def rechercher(self, brigand):
        return f"Qui peux me dire ou est partie le Brigand !! {brigand.recompense} $ à qui arrêtera {brigand.quelEstTonNom()} mort ou vif !"

    def presentation(self):
        base_presentation = super().sepresenter()
        specific_presentation = (
            f"Je suis Shérif {self.quelEstTonNom()} et j'ai coffré {self.brigand_coffres} brigands !"
        )
        return f"{base_presentation}\n{specific_presentation}\n"
