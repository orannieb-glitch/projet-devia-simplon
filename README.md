# Projet Simplon - Analyse des Ventes d'une PME (Développeur IA Agentique)

Ce projet a été réalisé dans le cadre de la sélection pour la formation **« Développeur en Intelligence Artificielle (IA Agentique) »** de Simplon.

Il propose une analyse exploratoire, relationnelle (SQL) et visuelle (Python / Plotly Express) des données de vente sur 20 jours d'une PME commerciale.

---

## 🎯 Objectifs du projet
1. **Explorer et valider** un jeu de données de ventes (qualité, cohérence, métriques clés).
2. **Interroger la base de données avec SQL** (SQLite) pour extraire les indicateurs d'activité (CA total, ventilation par produit et par région).
3. **Créer des visualisations interactives avec Python** (`pandas` & `plotly.express`) pour communiquer efficacement les insights aux décideurs.
4. **Formuler des recommandations stratégiques concrètes** pour orienter la politique commerciale de la PME.

---

## 📁 Structure du dépôt

```text
├── README.md               # Présentation du projet et consignes d'exécution
├── app.py                  # Script Python principal de traitement et génération des graphiques Plotly
├── requetes.sql            # Script SQL contenant toutes les requêtes d'analyse commentées
├── requirements.txt        # Dépendances Python nécessaires (pandas, plotly)
├── ventes.csv              # Jeu de données source des ventes (39 transactions, 20 jours)
├── fiche_synthese.md       # Synthèse des résultats et recommandations business
├── .devcontainer/          # Configuration pour exécution immédiate dans GitHub Codespaces
└── .gitignore              # Exclusion des fichiers temporaires et environnements virtuels
```

---

## 📊 Principaux résultats d'analyse

| Indicateur | Valeur clé | Détail / Observation |
| :--- | :--- | :--- |
| **Chiffre d'affaires total** | **44 825 €** | Réparti sur 39 transactions du 01/01/2022 au 20/01/2022 |
| **Volume total vendu** | **3 380 unités** | Réparties sur 3 références produits et 2 régions |
| **Produit leader en volume** | **Produit A (1 750 unités)** | 51,8 % des volumes, CA de 17 500 € (prix : 10 €) |
| **Produit leader en valeur** | **Produit A (17 500 €)** | Suivi de près par le **Produit B** (15 825 €, 35,3 % du CA) |
| **Produit à forte rentabilité**| **Produit C (20 €/u)** | Bien que représentant 17 % du volume, génère plus de 25 % du CA |
| **Répartition géographique** | **Sud (53,8 %) / Nord (46,2 %)** | La région Sud surperforme légèrement en valeur (24 100 € vs 20 725 €) |

---

## 🚀 Démarrage rapide

### Dans GitHub Codespaces (Recommandé par Simplon)
1. Cliquez sur le bouton vert **Code**, puis sélectionnez l'onglet **Codespaces**.
2. Cliquez sur **Create codespace on main**.
3. Une fois l'environnement chargé, ouvrez le terminal (`Ctrl + ~`).
4. Lancez le script de génération des graphiques :
   ```bash
   python3 app.py
   ```
5. Cliquez sur le bouton **🏠 PREVIEW** en bas de page pour observer les graphiques web interactifs générés (`ventes-par-produit.html`, `ca-par-produit.html`, `ventes-par-region.html`).

---

## 🛠️ Outils et technologies
- **SGBD & SQL** : SQLite / [SQLiteOnline](https://sqliteonline.com/)
- **Langage de script** : Python 3.11
- **Manipulation de données** : `pandas`
- **Visualisation interactive** : `plotly.express`
- **Contrôle de version** : Git & GitHub
