import tkinter as tk
from tkinter import Toplevel, Button, Label, Frame
import qrcode
from PIL import Image, ImageTk
import json

# BLOC F – Affichage récapitulatif + QR
def afficher_reservation_popup(recap_dict, parent=None):
    try:
        # Popup lié à la fenêtre principale
        popup = Toplevel(parent if parent else None)
        popup.title(f"Récapitulatif {recap_dict['id']}")
        popup.geometry("520x380")
        popup.resizable(False, False)

        # Forcer l'affichage au premier plan
        popup.transient(parent)  # lier au parent Tk
        popup.lift()
        popup.focus_force()
        popup.grab_set()

        # Contenu JSON lisible
        recap_text = json.dumps(recap_dict, indent=2, ensure_ascii=False)

        text_frame = Frame(popup)
        text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        label_text = Label(
            text_frame,
            text=recap_text,
            justify="left",
            font=("Courier", 10),
            anchor="nw"
        )
        label_text.pack(fill="both", expand=True)

        # QR Code frame
        qr_frame = Frame(popup)
        qr_frame.pack(side="right", padx=10, pady=10)

        qr_content = (
            f"ID: {recap_dict['id']}\n"
            f"Trajet: {recap_dict['trajet']}\n"
            f"Bus: {recap_dict['bus']}\n"
            f"Places: {', '.join(recap_dict['places'])}\n"
            f"Date: {recap_dict['date']}\n"
            f"Heure: {recap_dict['heure']}"
        )

        # Génération du QR code
        img = qrcode.make(qr_content).convert("RGB").resize((130, 130))
        qr_image = ImageTk.PhotoImage(img)

        qr_label = Label(qr_frame, image=qr_image)
        qr_label.image = qr_image  # garder la référence !
        qr_label.pack()

        # Bouton de fermeture
        Button(popup, text="Fermer", command=popup.destroy).pack(side="bottom", pady=10)

    except Exception as e:
        print("❌ Erreur affichage popup :", e)