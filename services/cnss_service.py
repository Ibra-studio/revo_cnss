from database.connection import get_connection
from services.employee_service import get_tous_les_employes
from datetime import datetime

TAUX_SALARIAL=0.06
TAUX_PATRONAL=0.19

def calculer_cotisation_salarial(salaire_brut):
    return salaire_brut*TAUX_SALARIAL
def calculer_cotisation_patronal(salaire_brut):
    return salaire_brut*TAUX_PATRONAL
def creer_declaration(mois,annee):
    conn=get_connection()
    cursor=conn.cursor()

    try:
     cursor.execute(
        "INSERT INTO declarations_cnss(mois,annee,date_generation) VALUES(?,?,?)",
        (mois,annee,str(datetime.now()))
    )
     declarationId=cursor.lastrowid

     employes=get_tous_les_employes()

    

     for e in employes:
       cursor.execute(
        "INSERT INTO lignes_declaration(declaration_id,employe_id,salaire_mois,cotisation_salariale,cotisation_patronale) VALUES(?,?,?,?,?)",
        (declarationId,e["id"],e["salaire_brut"],calculer_cotisation_salarial(e["salaire_brut"]),calculer_cotisation_patronal(e["salaire_brut"]))
    )
    
     conn.commit()
     return declarationId
    except Exception as e:
       conn.rollback()
       print(f"Erreur: {e}")
       return None


