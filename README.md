# Bordereau CNSS — REVO-LUTION Paie

Module de génération du bordereau CNSS mensuel développé en Python desktop.

## Stack technique
- Python 3.x
- Tkinter (interface graphique)
- SQLite (base de données locale)
- Reportlab (export PDF)
- Pytest (tests unitaires)

## Fonctionnalités
- Ajout et gestion des employés
- Calcul automatique des cotisations CNSS
  - Cotisation salariale : 6% du salaire brut
  - Cotisation patronale : 19% du salaire brut
- Génération de déclaration mensuelle
- Export PDF du bordereau
- Tests unitaires sur les calculs

## Installation

```bash
git clone <url-du-repo>
cd revo_cnss
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
