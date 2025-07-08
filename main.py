from controle.gestion_transport import GestionTransport
from controle.gestion_vehicule import GestionVehicules
from modele.vehicule import Vehicule
from interface.app_transport import ApplicationTransport

if __name__ == "__main__":
    gestion_transport = GestionTransport()
    gestion_vehicules = GestionVehicules()

    gestion_vehicules.ajouter(Vehicule("Bus A", []))
    gestion_vehicules.ajouter(Vehicule("Bus B", []))

    trajets = ["Centre → Université", "Marché → Gare"]
    bus_ids = ["Bus A", "Bus B"]

    app = ApplicationTransport(gestion_transport, gestion_vehicules, trajets, bus_ids)
    app.mainloop()