import tkinter as tk
from tkinter import Toplevel
import qrcode
from PIL import Image, ImageTk
import json

def afficher_reservation_popup(recap_dict):
    popup = Toplevel()
    popup.title(f"Récapitulatif {recap_dict['id']}")
    popup.geometry("500x320")
    popup.resizable(False, False)

    # JSON format
    recap_text = json.dumps(recap_dict, indent=2, ensure_ascii=False)

    # Zone texte
    text_frame = tk.Frame(popup)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    tk.Label(text_frame, text=recap_text, justify="left", font=("Courier", 10), anchor="nw").pack(fill="both", expand=True)

    # QR code
    qr_frame = tk.Frame(popup)
    qr_frame.pack(side="right", padx=10, pady=10)

    qr_content = (
        f"ID:{recap_dict['id']}\nTrajet:{recap_dict['trajet']}\nBus:{recap_dict['bus']}\n"
        f"Places:{','.join(recap_dict['places'])}\nDate:{recap_dict['date']}\nHeure:{recap_dict['heure']}"
    )
    img = qrcode.make(qr_content).convert("RGB").resize((130, 130))
    qr_image = ImageTk.PhotoImage(img)

    qr_label = tk.Label(qr_frame, image=qr_image)
    qr_label.image = qr_image
    qr_label.pack()