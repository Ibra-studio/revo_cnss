from tkinter import ttk
import os
from tkinter import simpledialog
from tkinter import messagebox
import tkinter as tk
from models.Employe import Employe
from services.employee_service import ajouter_employee,get_tous_les_employes
from services.cnss_service import creer_declaration
from export.bordereau import generer_bordereau_pdf

class MainWindow:

    def __init__(self,root):
        self.root=root
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=1)
        self.build_formulaire()
        self.build_tableau()
        self.build_boutons()

    def build_formulaire(self):
      # Titre
      frame=tk.Frame(self.root,padx=20,pady=20)
      frame.grid(row=0,column=0,sticky="nsew")
      
      tk.Label(frame, text="Ajouter un employé", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

      # Champs
      tk.Label(frame, text="Nom :").grid(row=1, column=0, sticky="e")
      self.entry_nom = tk.Entry(frame)
      self.entry_nom.grid(row=1, column=1, pady=5)

      tk.Label(frame, text="Prénom :").grid(row=2, column=0, sticky="e")
      self.entry_prenom = tk.Entry(frame)
      self.entry_prenom.grid(row=2, column=1, pady=5)

      tk.Label(frame, text="Poste :").grid(row=3, column=0, sticky="e")
      self.entry_poste = tk.Entry(frame)
      self.entry_poste.grid(row=3, column=1, pady=5)

      tk.Label(frame, text="Salaire brut :").grid(row=4, column=0, sticky="e")
      self.entry_salaire = tk.Entry(frame)
      self.entry_salaire.grid(row=4, column=1, pady=5)

      tk.Label(frame, text="Date embauche :").grid(row=5, column=0, sticky="e")
      self.entry_date = tk.Entry(frame)
      self.entry_date.grid(row=5, column=1, pady=5)

      # Bouton ajouter
      tk.Button(frame, text="Ajouter", command=self.ajouter_employe).grid(row=6, column=0, columnspan=2, pady=10)



    def build_tableau(self):
      frame=tk.Frame(self.root,padx=20,pady=20)
      frame.grid(row=1,column=0,sticky="nsew")
      frame.columnconfigure(0,weight=1)
      frame.columnconfigure(1,weight=1)
      colonnes = ("id", "nom", "prenom", "poste", "salaire_brut", "date_embauche")
    
      self.tableau = ttk.Treeview(frame, columns=colonnes, show="headings")
    
      scroll_x=ttk.Scrollbar(frame,orient="horizontal",command=self.tableau.xview)
      self.tableau.configure(xscrollcommand=scroll_x.set)

      # Définir les entêtes
      self.tableau.heading("id", text="ID")
      self.tableau.heading("nom", text="Nom")
      self.tableau.heading("prenom", text="Prénom")
      self.tableau.heading("poste", text="Poste")
      self.tableau.heading("salaire_brut", text="Salaire Brut")
      self.tableau.heading("date_embauche", text="Date Embauche")
    
      self.tableau.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
      scroll_x.grid(row=8,column=0,sticky="ew")
    
      self.rafraichir_tableau()

    def rafraichir_tableau(self):
      # Vider le tableau
      for row in self.tableau.get_children():
        self.tableau.delete(row)
    
      # Remplir avec les données
      employes = get_tous_les_employes()
      for e in employes:
        self.tableau.insert("", tk.END, values=(
            e["id"], e["nom"], e["prenom"], 
            e["poste"], e["salaire_brut"], e["date_embauche"]
        ))

    def build_boutons(self):
        tk.Button(self.root,text="Generer declarion CNSS",command=self.generer_declaration).grid(row=9,column=0,sticky="nw")
    def generer_declaration(self):
       self.root.focus_force()
       mois=simpledialog.askinteger("Mois","Entrez le mois (1-12):",parent=self.root)

       if mois is None:
          return
       self.root.focus_force()
       annee=simpledialog.askinteger("Annee","Entrez l'annee (20XX):",parent=self.root)

       if annee is None:
          return
      
       declaration_id=creer_declaration(mois,annee)
       if(declaration_id):
          filename=generer_bordereau_pdf(declaration_id,mois,annee)
          messagebox.showinfo("Succès","Declaration créee avec succès")
          os.startfile(filename)
       else:
          messagebox.showerror("Erreur","une erreur est survenu")

       
    def ajouter_employe(self):
        newEmploye=Employe(self.entry_nom.get(),self.entry_prenom.get(),self.entry_poste.get(),self.entry_salaire.get(),self.entry_date.get())
        ajouter_employee(newEmploye)
        self.entry_nom.delete(0,tk.END)
        self.entry_prenom.delete(0,tk.END)
        self.entry_poste.delete(0,tk.END)
        self.entry_salaire.delete(0,tk.END)
        self.entry_date.delete(0,tk.END)
        self.rafraichir_tableau()
   