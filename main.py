# Importation des classes nécessaires
from dame import Dame
from cowboy import Cowboy
from brigand import Brigand
from barman import Barman
from sherif import Sherif

# Initialisation des personnages
brigand = Brigand("Bob", dames_enlevees=5, recompense=500)
dame = Dame("Marianne", couleur_robe="rouge", etat=True)
cowboy = Cowboy("John", adjectif="intrépide", popularité=80)
barman = Barman("Arthur", name_bar="Le Saloon Doré")
sherif = Sherif("Wyatt", popularité=10)

# Début de l'histoire
print("Narrateur : Bienvenue à Nom-a-Change Western, un endroit où tout peut arriver...\n")
print("Le soir tombe sur la ville. Le Saloon Doré s'illumine, attirant les habitants pour une soirée animée.\n")
print(f"{barman.quelEstTonNom()} : {barman.presentation()}\n")

# Interaction entre les personnages au saloon
print("Narrateur : John, le cowboy intrépide, entre dans le saloon après une longue journée passée à protéger les fermiers locaux.\n")
print(f"{cowboy.presentation()}\n")
print(f"{cowboy.quelEstTonNom()} : {barman.quelEstTonNom()}, sers-moi un verre de {cowboy.quelEstTaBoisson()}. J'ai entendu des rumeurs inquiétantes...\n")
print(f"{barman.quelEstTonNom()} : Bien sûr, {cowboy.quelEstTonNom()}. Mais fais attention, {brigand.quelEstTonNom()} a été aperçu près du canyon des bandits. Une prime de {brigand.recompense}$ est sur sa tête.\n")

# Apparition du brigand
print("Narrateur : Alors que l'ambiance semble détendue, la porte du saloon s'ouvre violemment. Bob, le brigand, entre avec une aura menaçante.\n")
print(f"{brigand.quelEstTonNom()} : {brigand.presentation()}\n")
print(f"{brigand.quelEstTonNom()} : Où est {dame.quelEstTonNom()} ? Elle m’appartient maintenant ! Pas un geste, ou je sors mon revolver !\n")

# Kidnapping de Marianne
print("Narrateur : Bob se dirige vers Marianne, qui, paniquée, cherche de l'aide du regard.\n")
print(f"{cowboy.quelEstTonNom()} : {brigand.kidnapper(dame)}\n")
print("Narrateur : Avant que quelqu’un puisse réagir, Bob s’enfuit à cheval avec Marianne.\n")

# Intervention de John le cowboy
print("Narrateur : John finit son verre d’un trait et sort du saloon d’un pas rapide.\n")
print(f"{cowboy.quelEstTonNom()} : {barman.quelEstTonNom()}, appelle le shérif. Moi, je vais récupérer Marianne.\n")
print(f"{cowboy.quelEstTonNom()} : {cowboy.tirer(brigand)}\n")
print("Narrateur : Une balle frôle Bob, mais il parvient à disparaître dans l’obscurité avec sa captive.\n")

# Arrivée du shérif
print("Narrateur : Wyatt, le shérif, arrive peu après, alerté par les coups de feu.\n")
print(f"{sherif.quelEstTonNom()} : {sherif.presentation()}\n")
print(f"{sherif.quelEstTonNom()} : {sherif.quelEstTonNom()} : Alors, où est ce brigand ? Il ne perd rien pour attendre.\n")
print(f"{sherif.quelEstTonNom()} : {sherif.rechercher(brigand)}\n")

# Poursuite par le cowboy
print("Narrateur : Pendant ce temps, John suit les traces de Bob jusqu’au canyon des bandits.\n")
print(f"{cowboy.quelEstTonNom()} : {cowboy.tirer(brigand)}\n")
print(f"Narrateur : Après une bataille acharnée, John parvient à libérer Marianne.\n")
print(f"{cowboy.quelEstTonNom()} : {cowboy.delivrer(dame)}\n")

# Confrontation finale
print("Narrateur : Wyatt arrive juste à temps pour encercler Bob avec son équipe de shérifs adjoints.\n")
print(f"{sherif.quelEstTonNom()} : {sherif.tirer(brigand)}\n")
print("Narrateur : Bob, blessé et acculé, se rend finalement. Il est menotté par Wyatt et emmené en prison.\n")
print(f"{sherif.quelEstTonNom()} : {sherif.coffrer(brigand)}\n")
print(f"{sherif.quelEstTonNom()} : Bien joué, {cowboy.quelEstTonNom()}. Grâce à toi, Marianne est saine et sauve, et ce brigand est hors d’état de nuire.\n")

# Fin de l'histoire
print("Narrateur : La paix est temporairement rétablie à Nom-a-Change Western, mais dans cette ville, l’aventure ne dort jamais...\n")
