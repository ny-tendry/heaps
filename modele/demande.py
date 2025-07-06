class DemandeTransport: 
    def __init__(self, id_demande, trajet, priorite):
            self.id = id_demande
            self.trajet = trajet
            self.priorite = priorite

    def __lt__(self, other):
          return self.priorite > other.priorite