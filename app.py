"""
==============================================================================
PROJET SIMPLON : ANALYSE DES VENTES D'UNE PME (IA AGENTIQUE)
Génération des visualisations interactives avec pandas et Plotly Express
==============================================================================
"""

import pandas as pd
import plotly.express as px

# 1. Chargement des données
# On utilise l'URL officielle du CSV fournie dans le dépôt GitHub Simplon
URL_DATASET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'

try:
    donnees = pd.read_csv(URL_DATASET)
except Exception:
    # Solution de repli si pas de connexion internet : chargement du fichier local
    donnees = pd.read_csv('ventes.csv')

# 2. Enrichissement des données : calcul du Chiffre d'Affaires par transaction
# Chiffre d'affaires = Prix unitaire * Quantité vendue
donnees['chiffre_affaires'] = donnees['prix'] * donnees['qte']

print("Aperçu des données :")
print(donnees.head())
print(f"\nNombre total de transactions : {len(donnees)}")
print(f"Chiffre d'affaires total : {donnees['chiffre_affaires'].sum()} €")


# -----------------------------------------------------------------------------
# GRAPHIQUE 0 (Exemple du README d'origine) : Quantité vendue par région
# -----------------------------------------------------------------------------
fig_region = px.pie(
    donnees, 
    values='qte', 
    names='region', 
    title="Répartition des quantités vendues par région",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_region.update_traces(textposition='inside', textinfo='percent+label')
fig_region.write_html('ventes-par-region.html')
print("-> 'ventes-par-region.html' généré avec succès !")


# -----------------------------------------------------------------------------
# GRAPHIQUE 1 (Demande 6.a du brief) : Ventes (quantité) par produit
# -----------------------------------------------------------------------------
# On agrège les données par produit pour obtenir le volume total vendu
ventes_produit = donnees.groupby('produit', as_index=False)['qte'].sum()

fig_ventes_produit = px.bar(
    ventes_produit,
    x='produit',
    y='qte',
    text='qte',
    title="Quantités totales vendues par produit (Volume des ventes)",
    labels={'produit': 'Produit', 'qte': 'Unités vendues'},
    color='produit',
    color_discrete_sequence=px.colors.qualitative.Safe
)
# Mise en forme pour une lecture claire et professionnelle
fig_ventes_produit.update_traces(textposition='outside')
fig_ventes_produit.update_layout(
    xaxis_title="Type de produit",
    yaxis_title="Quantité totale vendue",
    showlegend=False
)
fig_ventes_produit.write_html('ventes-par-produit.html')
print("-> 'ventes-par-produit.html' généré avec succès !")


# -----------------------------------------------------------------------------
# GRAPHIQUE 2 (Demande 6.b du brief) : Chiffre d'affaires par produit
# -----------------------------------------------------------------------------
# On agrège les données par produit pour obtenir le CA total généré
ca_produit = donnees.groupby('produit', as_index=False)['chiffre_affaires'].sum()

fig_ca_produit = px.bar(
    ca_produit,
    x='produit',
    y='chiffre_affaires',
    text='chiffre_affaires',
    title="Chiffre d'affaires total par produit (en Euros)",
    labels={'produit': 'Produit', 'chiffre_affaires': "Chiffre d'affaires (€)"},
    color='produit',
    color_discrete_sequence=px.colors.qualitative.Bold
)
# Ajout du symbole € sur les étiquettes de données
fig_ca_produit.update_traces(
    texttemplate='%{text:,.0f} €',
    textposition='outside'
)
fig_ca_produit.update_layout(
    xaxis_title="Type de produit",
    yaxis_title="Chiffre d'affaires (€)",
    showlegend=False
)
fig_ca_produit.write_html('ca-par-produit.html')
print("-> 'ca-par-produit.html' généré avec succès !")


print("\n[SUCCÈS] Tous les graphiques ont été générés au format HTML.")
