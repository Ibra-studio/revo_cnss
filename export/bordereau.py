from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from database.connection import get_connection

def generer_bordereau_pdf(declaration_id, mois, annee):
    filename = f"bordereau_cnss_{mois}_{annee}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Titre
    elements.append(Paragraph(f"Bordereau CNSS — {mois}/{annee}", styles["Title"]))
    elements.append(Spacer(1, 20))

    # Récupérer les lignes de la déclaration
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.nom, e.prenom, l.salaire_mois, l.cotisation_salariale, l.cotisation_patronale
        FROM lignes_declaration l
        JOIN employes e ON l.employe_id = e.id
        WHERE l.declaration_id = ?
    """, (declaration_id,))
    lignes = cursor.fetchall()

    # Construire le tableau
    data = [["Nom", "Prénom", "Salaire Brut", "Cot. Salariale", "Cot. Patronale"]]
    
    total_salaire = 0
    total_salarial = 0
    total_patronal = 0

    for li in lignes:
        data.append([li["nom"], li["prenom"], f"{li['salaire_mois']} FCFA",
                     f"{li['cotisation_salariale']} FCFA", f"{li['cotisation_patronale']} FCFA"])
        total_salaire += li["salaire_mois"]
        total_salarial += li["cotisation_salariale"]
        total_patronal += li["cotisation_patronale"]

    # Ligne totaux
    data.append(["TOTAL", "", f"{total_salaire} FCFA", f"{total_salarial} FCFA", f"{total_patronal} FCFA"])

    # Style du tableau
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, -1), (-1, -1), colors.lightgrey),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
    ]))

    elements.append(table)
    doc.build(elements)
    return filename
