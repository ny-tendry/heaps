from controle.gestion_transport import GestionTransport
from controle.gestion_vehicule import GestionVehicules
from modele.vehicule import Vehicule
from interface.app_transport import ApplicationTransport
from db_transport import initialiser_base  # Crée la base si elle n’existe pas

if __name__ == "__main__":
    initialiser_base()

    gestion_transport = GestionTransport()
    gestion_vehicules = GestionVehicules()

    # Ajout des bus
    gestion_vehicules.ajouter(Vehicule("Bus A", []))
    gestion_vehicules.ajouter(Vehicule("Bus B", []))

    trajets = ["Centre -> Universitaire", "Marché -> Gare"]
    bus_ids = ["Bus A", "Bus B"]

    # Lancement de l’application
    app = ApplicationTransport(gestion_transport, gestion_vehicules, trajets, bus_ids)
    app.mainloop()