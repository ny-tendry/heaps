#controle/gestion_vehicules.py
from modele.vehicule import Vehicule

class GestionVehicules:
        def __init__(self):
                self.vehicules = {}

        #fonction pour l'ajout
        def ajouter(self, vehicule):
                self.vehicules[vehicule.id] = vehicule

        #fonction pour les places        
        def place(self, id_vehicule):
                return self.vehicules[id_vehicule].places if id_vehicule in self.vehicules else []

        #fonction pour reserver
        def reserver(self, id_vehicule, place):
                if id_vehicule in self.vehicules and place in self.vehicules[id_vehicule].places:
                        self.vehicules[id_vehicule].places.remove(place)
                        return True
                return False