from humain import Humain

class Brigand(Humain):
    def __init__(self, name, look="méchant", dames_enlevees=0, recompense=100, en_prison=False):
        super().__init__(name, drink="tord-boyaux")
        self.look = look
        self.dames_enlevees = dames_enlevees
        self.recompense = recompense
        self.en_prison = en_prison

    def manger(self):
        return f"{self.quelEstTonNom()} mange un morceau de viande séchée, c'est tout ce qu'il peut trouver dans le désert !"

    def kidnapper(self, dame):
        if dame.etat:
            dame.kidnapper()
            self.dames_enlevees += 1
            return f"Ah ah! {dame.quelEstTonNom()}, tu es mienne désormais!"
        return f"{dame.quelEstTonNom()} est déjà captive!"
    
    def connaitreRecompense(self):
        return f"La récompense pour capturer {self.quelEstTonNom()} est de {self.recompense} $."
    
    def emprisonner(self, sherif):
        if not self.en_prison:
            self.en_prison = True
            return f"Damned, je suis fait ! {sherif.name}, tu m’as eu !"
        return f"{self.quelEstTonNom()} est déjà en prison, gardé par le Shérif {sherif.name}."
    
    def presentation(self):
        base_presenter = super().sepresenter()
        specific_presentation = (
            f" J’ai l’air {self.look} et j’ai déjà kidnappé {self.dames_enlevees} dames !\n"
            f" Ma tête est mise à prix {self.recompense} $ !\n"
        )
        return f"{base_presenter}\n{specific_presentation}\n"
