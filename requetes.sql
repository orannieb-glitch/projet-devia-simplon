-- ==============================================================================
-- PROJET SIMPLON : ANALYSE DES VENTES D'UNE PME
-- Fichier de requêtes SQL pour SQLite (SQLiteOnline)
-- Table : ventes (colonnes: date, produit, prix, qte, region)
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- Étape 2 : Requête de vérification après import du fichier CSV
-- ------------------------------------------------------------------------------
-- Objectif : Vérifier que les 39 enregistrements ont bien été importés
-- et visualiser la structure des données.
SELECT * 
FROM ventes 
LIMIT 10;

-- Contrôle du volume total de lignes importées (doit retourner 39)
SELECT COUNT(*) AS nombre_de_lignes 
FROM ventes;


-- ------------------------------------------------------------------------------
-- Question 3.a : Chiffre d'affaires total
-- ------------------------------------------------------------------------------
-- Objectif : Calculer le montant global généré par l'ensemble des ventes sur les 20 jours.
-- Méthode : Chaque ligne représente une transaction où l'on multiplie le prix unitaire
-- par la quantité vendue, puis on additionne le tout via la fonction d'agrégation SUM().
SELECT 
    SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;
-- Résultat attendu : 44 825 €


-- ------------------------------------------------------------------------------
-- Question 3.b : Ventes par produit (Quantité vendue et Chiffre d'affaires)
-- ------------------------------------------------------------------------------
-- Objectif : Mesurer la performance commerciale de chaque référence de produit.
-- Méthode : On groupe par nom de produit. On calcule à la fois le volume total (SUM(qte))
-- et la valeur totale (SUM(prix * qte)), triés par chiffre d'affaires décroissant.
SELECT 
    produit,
    SUM(qte) AS quantite_totale,
    SUM(prix * qte) AS chiffre_affaires,
    ROUND(SUM(prix * qte) * 100.0 / (SELECT SUM(prix * qte) FROM ventes), 2) AS part_ca_pourcentage
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC;
-- Résultats attendus :
-- 1. Produit A : 1 750 unités | 17 500 € (39.04 %)
-- 2. Produit B : 1 055 unités | 15 825 € (35.30 %)
-- 3. Produit C :   575 unités | 11 500 € (25.66 %)


-- ------------------------------------------------------------------------------
-- Question 3.c : Ventes par région (Quantité vendue et Chiffre d'affaires)
-- ------------------------------------------------------------------------------
-- Objectif : Comparer la dynamique commerciale entre les zones géographiques (Nord vs Sud).
-- Méthode : On agrège par la colonne "region" pour obtenir les volumes et le CA par zone.
SELECT 
    region,
    SUM(qte) AS quantite_totale,
    SUM(prix * qte) AS chiffre_affaires,
    ROUND(SUM(prix * qte) * 100.0 / (SELECT SUM(prix * qte) FROM ventes), 2) AS part_ca_pourcentage
FROM ventes
GROUP BY region
ORDER BY chiffre_affaires DESC;
-- Résultats attendus :
-- 1. Sud  : 1 775 unités | 24 100 € (53.76 %)
-- 2. Nord : 1 605 unités | 20 725 € (46.24 %)


-- ------------------------------------------------------------------------------
-- Requête Bonus : Analyse croisée Produit x Région
-- ------------------------------------------------------------------------------
-- Objectif : Identifier si certains produits sous-performent dans une région spécifique.
SELECT 
    produit,
    region,
    SUM(qte) AS quantite_vendue,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit, region
ORDER BY produit, region;
