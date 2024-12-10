from humain import Humain

class Dame(Humain):
    def __init__(self, name, couleur_robe, etat=False):
        super().__init__(name, drink = "lait")
        self.couleur_robe = couleur_robe
        self.etat = etat

    def manger(self):
        return f"{self.quelEstTonNom()} mange une salade accompagnée de pain frais !"
    
    def kidnapper(self):
        if self.etat == False: 
            return "Aaaaah! Aidez-moi, je suis kidnappée!"
        else:
            return "Je suis déjà captive!"
        
    def libérer(self, cowboy):
        if self.etat:
            self.etat = False 
            return f"Merci {cowboy.quelEstTonNom()} de m'avoir libérée!"
        else:
            return "Je suis déjà libre!"

    def changerRobe(self, nouvelle_robe): 
        self.couleur_robe = nouvelle_robe
        return f"Regardez ma nouvelle robe {self.couleur_robe} !"
    
    def presentation(self):
        base_presentation = super().sepresenter()
        specific_presentation = (
            f"Ma robe et de la couleur {self.couleur_robe}"
        )
        return f"{base_presentation}\n{specific_presentation}\n"