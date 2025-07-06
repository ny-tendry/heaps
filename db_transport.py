import sqlite3
from datetime import datetime

def connecter():
    conn = sqlite3.connect("transport.db")
    return conn

def initialiser_base():
    conn = connecter()
    curseur = conn.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id TEXT PRIMARY KEY,
            trajet TEXT,
            bus TEXT,
            places TEXT,
            date_depart TEXT,
            heure_depart TEXT,
            horodatage TEXT
        )
    """)
    conn.commit()
    conn.close()

def ajouter_reservation(data):
    conn = connecter()
    curseur = conn.cursor()
    curseur.execute("""
        INSERT INTO reservations (id, trajet, bus, places, date_depart, heure_depart, horodatage)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["id"],
        data["trajet"],
        data["bus"],
        ",".join(data["places"]),
        data["date"],
        data["heure"],
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()