class Pokemon:
    def __init__(self, nom, point_de_vie, type, poids, taille, environnement, description):
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.type = type  # feu, eau, plante, normal
        self.poids = poids
        self.taille = taille
        self.environnement = environnement
        self.description = description
        self.niveau = 1  # Niveau initial
        self.statut_bar_exp = 0  # Barre d'expérience initiale

     
    
    def gagner_experience(self, experience):
        self.statut_bar_exp += experience
        if self.statut_bar_exp >= 100:  # Condition barre_exp
            self.niveau += 1
            self.statut_bar_exp = 0
            print(f"{self.nom} est passé niveau {self.niveau}!")