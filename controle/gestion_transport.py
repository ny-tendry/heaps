# controle/gestion_transport.py
import heapq
from modele.demande import DemandeTransport

class GestionTransport:
    def __init__(self):
        self.file_prioritaire = []

    # Ajout de demande
    def ajouter_demande(self, demande):
        heapq.heappush(self.file_prioritaire, demande)

    # Traitement de la prochaine
    def traiter_prochaine(self):
        return heapq.heappop(self.file_prioritaire) if self.file_prioritaire else None