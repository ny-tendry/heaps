import tkinter as tk
from tkinter import messagebox
from modele.demande import DemandeTransport
from interface.reservation import afficher_reservation_popup  # Module popup QR
from db_transport import ajouter_reservation  # Sauvegarde dans SQLite

class ApplicationTransport(tk.Tk):
    def __init__(self, gestion_transport, gestion_vehicules, trajets, bus_ids):
        super().__init__()
        self.title("Réservation Transport")
        self.geometry("750x600")

        self.gestion_transport = gestion_transport
        self.gestion_vehicules = gestion_vehicules
        self.trajets = trajets
        self.bus_ids = bus_ids

        self.itineraire_var = tk.StringVar(value="Choisir le trajet")
        self.bus_var = tk.StringVar(value="Choisissez votre Bus")
        self.date_depart_var = tk.StringVar(value="07/07/2025")
        self.heure_depart_var = tk.StringVar(value="08:30")
        self.places_selectionnees = []
        self.reservation_count = 0

        self.creer_interface()

    def creer_interface(self):
        main_frame = tk.Frame(self)
        main_frame.pack(pady=10)

        top_frame = tk.Frame(main_frame)
        top_frame.pack()

        tk.Label(top_frame, text="Trajet :").grid(row=0, column=0)
        tk.OptionMenu(top_frame, self.itineraire_var, *(["Choisir le trajet"] + self.trajets)).grid(row=0, column=1)

        tk.Label(top_frame, text="Bus :").grid(row=0, column=2)
        tk.OptionMenu(top_frame, self.bus_var, *(["Choisissez votre Bus"] + self.bus_ids)).grid(row=0, column=3)

        date_heure_frame = tk.Frame(main_frame)
        date_heure_frame.pack(pady=5)

        tk.Label(date_heure_frame, text="Date départ :").grid(row=0, column=0)
        tk.Entry(date_heure_frame, textvariable=self.date_depart_var, width=12).grid(row=0, column=1)

        tk.Label(date_heure_frame, text="Heure départ :").grid(row=0, column=2)
        tk.Entry(date_heure_frame, textvariable=self.heure_depart_var, width=8).grid(row=0, column=3)

        tk.Label(main_frame, text="Choisissez vos places :").pack(pady=10)
        self.places_frame = tk.Frame(main_frame)
        self.places_frame.pack()

        tk.Button(main_frame, text="Réserver", command=self.reserver).pack(pady=10)

        self.bus_var.trace_add("write", lambda *args: self.mettre_a_jour_place())
        self.itineraire_var.trace_add("write", lambda *args: self.mettre_a_jour_place())
        self.mettre_a_jour_place()

    def mettre_a_jour_place(self):
        for widget in self.places_frame.winfo_children():
            widget.destroy()
        self.places_selectionnees.clear()

        bus_id = self.bus_var.get()
        if bus_id not in self.bus_ids:
            return

        places = [f"P{i+1}" for i in range(32)]
        vehicule = self.gestion_vehicules.vehicules.get(bus_id)
        if vehicule and not vehicule.places:
            vehicule.places = places.copy()

        places_libres = set(self.gestion_vehicules.place(bus_id))
        self.place_buttons = {}

        for row in range(4):
            for col in range(8):
                idx = row * 8 + col
                nom = places[idx]
                couleur = "green" if nom in places_libres else "red"
                btn = tk.Button(self.places_frame, text=nom, width=5, bg=couleur)
                btn.grid(row=row, column=col, padx=3, pady=2)
                if couleur == "green":
                    btn.config(command=lambda n=nom: self.selectionner_place(n))
                self.place_buttons[nom] = btn

    def selectionner_place(self, nom):
        btn = self.place_buttons[nom]
        if btn["bg"] == "green":
            btn.config(bg="orange")
            self.places_selectionnees.append(nom)
        elif btn["bg"] == "orange":
            btn.config(bg="green")
            self.places_selectionnees.remove(nom)

    def reserver(self):
        trajet = self.itineraire_var.get()
        bus_id = self.bus_var.get()
        date = self.date_depart_var.get()
        heure = self.heure_depart_var.get()
        places = self.places_selectionnees

        if trajet == "Choisir le trajet" or bus_id == "Choisissez votre Bus" or not places or not date or not heure:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        indispo = [p for p in places if p not in self.gestion_vehicules.place(bus_id)]
        if indispo:
            messagebox.showerror("Erreur", f"Places déjà prises : {', '.join(indispo)}")
            return

        confirm = messagebox.askyesno("Confirmation", f"Confirmer la réservation des places : {', '.join(places)} ?")
        if not confirm:
            return

        for p in places:
            self.gestion_vehicules.reserver(bus_id, p)

        self.reservation_count += 1
        reservation_id = f"R{self.reservation_count:04d}"
        demande = DemandeTransport(reservation_id, trajet, priorite=1)
        self.gestion_transport.ajouter_demande(demande)

        recap_dict = {
            "id": reservation_id,
            "trajet": trajet,
            "bus": bus_id,
            "places": places,
            "date": date,
            "heure": heure
        }

        ajouter_reservation(recap_dict)
        afficher_reservation_popup(recap_dict)

        self.mettre_a_jour_place()