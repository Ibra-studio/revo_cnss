from database.connection import get_connection

def ajouter_employee(employee):
    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        "INSERT INTO employes(nom,prenom,poste,salaire_brut,date_embauche) VALUES(?,?,?,?,?)",
        (employee.nom,employee.prenom,employee.poste,employee.salaire_brut,employee.date_embauche)
    )
    conn.commit()
def get_tous_les_employes():
    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        "SELECT * FROM employes"
        
    )
    return cursor.fetchall()
def modifier_employee(employee):
    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute(
        "UPDATE employes SET nom=(?),prenom=(?),poste=(?),salaire_brut=(?),date_embauche=(?) WHERE id=(?)",
        (employee.nom,employee.prenom,employee.poste,employee.salaire_brut,employee.date_embauche,employee.id)
    )
    conn.commit()

def supprimer_employee(employeeId):
     conn=get_connection()
     cursor=conn.cursor()


     cursor.execute(
        "DELETE FROM employes WHERE id=(?)",
        (employeeId,)
     )
     conn.commit()