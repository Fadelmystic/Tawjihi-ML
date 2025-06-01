# Dataset des Établissements d'Enseignement Supérieur au Maroc

Ce projet présente une base de données structurée des établissements d'enseignement supérieur au Maroc, générée à partir du guide Tawjihi.

## Description du Projet

Ce projet a consisté en la transformation des données du guide Tawjihi en une base de données structurée et exploitable. Le processus s'est déroulé en plusieurs étapes :

1. **Source des Données**
   - Extraction des informations depuis le fichier PDF du guide Tawjihi
   - Le guide contient les informations détaillées sur les établissements d'enseignement supérieur au Maroc

2. **Processus de Transformation**
   - Conversion des données du PDF vers un format JSON structuré
   - Le format JSON permet une meilleure organisation et structuration des données
   - Les informations sont catégorisées et standardisées

3. **Formats Finaux**
   - Génération de fichiers CSV pour une utilisation facile dans différents outils
   - Les données sont organisées de manière claire et accessible

## Structure des Données

Les données sont structurées avec les champs suivants pour chaque établissement :
- **Écoles/Instituts** : Nom complet de l'établissement
- **Ville** : Localisation(s) de l'établissement
- **Type d'établissement** : Catégorie (ex: Université publique)
- **Diplôme** : Niveaux de diplômes proposés (Licence, Master, Doctorat)
- **Durée d'études** : Durée pour chaque niveau de diplôme
- **Conditions d'accès** : Prérequis pour l'admission
- **Filières Bacs acceptées** : Types de baccalauréats acceptés
- **Seuil** : Critères de sélection et conditions d'admission
- **Filières d'études possibles** : Liste des spécialisations disponibles

## Nettoyage et Analyse des Données

Le notebook `TAWJIHI-ML-Analysis.ipynb` contient le processus complet de nettoyage et d'analyse des données :

1. **Nettoyage des Données**
   - Standardisation des valeurs manquantes
   - Nettoyage du texte
   - Traitement des seuils d'admission
   - Détection des doublons

2. **Analyse des Seuils d'Admission**
   - Conservation des seuils 2023 et 2024
   - Remplissage intelligent des valeurs manquantes
   - Analyse statistique par type d'établissement
   - Visualisations des distributions

## Utilisation des Données

Les données générées peuvent être utilisées pour :
- L'analyse des établissements d'enseignement supérieur au Maroc
- La recherche et la comparaison des filières disponibles
- L'aide à la décision pour les futurs étudiants
- Des études statistiques sur l'enseignement supérieur

## Fichiers Disponibles

1. **Données Brutes**
   - `data_expanded.csv` : Données extraites du guide Tawjihi

2. **Données Nettoyées**
   - `data_expanded_cleaned.csv` : Données nettoyées et prêtes à l'analyse

3. **Analyse**
   - `TAWJIHI-ML-Analysis.ipynb` : Notebook contenant le code de nettoyage et d'analyse

## Installation et Utilisation

1. **Installation des Dépendances**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. **Analyse Interactive**
   - Ouvrir `TAWJIHI-ML-Analysis.ipynb` dans Jupyter Notebook
   - Exécuter les cellules pour le nettoyage et l'analyse 