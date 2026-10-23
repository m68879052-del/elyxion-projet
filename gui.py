import customtkinter as ctk
import threading
import os
import sys
import requests
from tkinter import messagebox

from api.main import calculer_devis_complet, exporter_pdf_elyxion, generer_visuel_elyxion


class ElyxionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- CONFIGURATION FENÊTRE ---
        self.title("ELYXION EMPIRE - STATION EXPERT V3")
        self.after(0, lambda: self.state('zoomed'))
        self.configure(fg_color="#07090F")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (CONTRÔLES) ---
        self.sidebar = ctk.CTkScrollableFrame(self, width=400, fg_color="#0F121F", corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        
        ctk.CTkLabel(self.sidebar, text="ELYXION", font=("Impact", 60), text_color="#D4AF37").pack(pady=20)

        # --- SECTION ARCHITECTURE ---
        self._section("ARCHITECTURE")
        self.long = self._input("Longueur terrain (m)", "15")
        self.larg = self._input("Largeur terrain (m)", "20")
        self.haut = self._input("Niveaux (R+N)", "1")
        self.ch = self._input("Chambres", "4")
        self.sal = self._input("Salons", "2")
        self.dou = self._input("Douches", "3")

        # --- SECTION MERCURIALE GNF ---
        self._section("MERCURIALE GNF")
        self.p_cim = self._input("Ciment (Sac)", "85000")
        self.p_sab = self._input("Sable (m3/Camion)", "1200000")
        self.p_gra = self._input("Gravier (m3/Camion)", "1500000")
        self.p_fer = self._input("Fer (Tonne)", "12000")
        self.p_bri = self._input("Brique (Unité)", "4500")

        # --- CHOIX DU MODÈLE ---
        self._section("MODÈLE DE BÂTIMENT")
        self.type_v = ctk.StringVar(value="Villa Moderne")
        ctk.CTkOptionMenu(self.sidebar, 
                         values=["Villa Moderne", "Immeuble", "Hôtel", "Duplex", "Entrepôt"], 
                         variable=self.type_v,
                         fg_color="#1E40AF").pack(pady=10, fill="x", padx=40)
        
        self.std_v = ctk.StringVar(value="Standard")
        ctk.CTkSegmentedButton(self.sidebar, 
                              values=["Éco", "Standard", "Luxe"], 
                              variable=self.std_v,
                              selected_color="#22C55E").pack(pady=10, fill="x", padx=40)

        # --- ZONE CENTRALE ---
        self.view = ctk.CTkFrame(self, fg_color="transparent")
        self.view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.view.grid_columnconfigure(0, weight=1)
        self.view.grid_rowconfigure(0, weight=1)

        self.txt = ctk.CTkTextbox(self.view, font=("Consolas", 16), border_color="#1E40AF", border_width=2)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # --- BARRE DE COMMANDE ---
        self.cmd = ctk.CTkFrame(self, fg_color="#0F121F", height=150)
        self.cmd.grid(row=1, column=1, sticky="ew", padx=20, pady=20)
        
        self.entry = ctk.CTkEntry(self.cmd, placeholder_text="Posez votre question technique ici...", height=50, font=("Arial", 16))
        self.entry.pack(fill="x", padx=30, pady=20)

        btn_box = ctk.CTkFrame(self.cmd, fg_color="transparent")
        btn_box.pack(fill="x", padx=30, pady=(0, 20))
        
        ctk.CTkButton(btn_box, text="CALCULER DEVIS", fg_color="#22C55E", height=45, command=self.run_ia).pack(side="left", expand=True, padx=10)
        ctk.CTkButton(btn_box, text="EXPORTER PDF", fg_color="#E67E22", height=45, command=self.run_pdf).pack(side="left", expand=True, padx=10)

    # Utilitaires
    def _section(self, text):
        ctk.CTkLabel(self.sidebar, text=f"--- {text} ---", font=("Arial", 13, "bold"), text_color="#D4AF37").pack(pady=(15, 5))

    def _input(self, label, default):
        ctk.CTkLabel(self.sidebar, text=label, font=("Arial", 11), text_color="#AAAAAA").pack(anchor="w", padx=45)
        e = ctk.CTkEntry(self.sidebar, height=35)
        e.insert(0, default)
        e.pack(fill="x", padx=40, pady=2)
        return e

    def get_data(self):
        return {
            "long": self.long.get(), "larg": self.larg.get(), "haut": self.haut.get(),
            "ch": self.ch.get(), "sal": self.sal.get(), "dou": self.dou.get(),
            "p_cim": self.p_cim.get(), "p_sab": self.p_sab.get(), "p_gra": self.p_gra.get(),
            "p_fer": self.p_fer.get(), "p_bri": self.p_bri.get(),
            "type": self.type_v.get(), "standing": self.std_v.get()
        }

    def run_ia(self):
        self.txt.insert("end", f"\n[ELYXION] Analyse du projet {self.type_v.get()} en cours...\n")
        threading.Thread(target=self._task_ia, daemon=True).start()

    def _task_ia(self):
        res = calculer_devis_complet(self.entry.get(), self.get_data())
        self.after(0, lambda: self.txt.insert("end", f"\n{res}\n{'-'*40}\n"))

            def run_pdf(self):
        path = exporter_pdf_elyxion(self.txt.get("1.0", "end"))
        if path:
            import platform
            import subprocess
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])



def check_ollama():
    try:
        return requests.get("http://localhost:11434/", timeout=2).status_code == 200
    except: return False

if __name__ == "__main__":
    if check_ollama():
        app = ElyxionApp()
        app.mainloop()
    else:
        root = ctk.CTk(); root.withdraw()
        messagebox.showerror("ERREUR", "Ollama n'est pas lancé.")
        root.destroy()