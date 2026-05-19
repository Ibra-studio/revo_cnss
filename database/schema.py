from database.connection import get_connection

def create_tables():
    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""  
          CREATE TABLE IF NOT EXISTS utilisateur (
                   id INTEGER PRIMARY KEY AUTOiNCREMENT,
                   nom TEXT NOT NULL,
                   mot_de_passe TEXT NOT NULL,
                   role TEXT NOT NULL
                   )

      """)
    
    cursor.execute("""  
          CREATE TABLE IF NOT EXISTS employes (
                   id INTEGER PRIMARY KEY AUTOiNCREMENT,
                   non TEXT NOT NULL,
                   prenom TEXT NOT NULL,
                   poste TEXT NOT NULL,
                   salaire_brut REAL NOT NULL,
                   date_embauche REAL NOT NULL
                   )

      """)
    cursor.execute("""  
          CREATE TABLE IF NOT EXISTS declarations_cnss (
                   id INTEGER PRIMARY KEY AUTOiNCREMENT,
                   mois INTEGER NOT NULL,
                   annee INTEGER NOT NULL,
                   date_generation TEXT NOT NULL)
                   """)
    cursor.execute("""  
          CREATE TABLE IF NOT EXISTS lignes_declaration (
                   id INTEGER PRIMARY KEY AUTOiNCREMENT,
                   declaration_id INTEGER NOT NULL,
                   employe_id INTEGER NOT NULL,
                   salaire_mois REAL NOT NULL,
                   cotisation_salariale REAL NOT NULL,
                   cotisation_patronale REAL NOT NULL,
                   FOREIGN KEY (declaration_id) REFERENCES declarations_cnss(id),
                   FOREIGN KEY (employe_id) REFERENCES employes(id))
                   """)
    conn.commit()