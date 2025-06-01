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
   - Création de fichiers Excel (XLSX) pour une visualisation et manipulation aisée
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

## Utilisation des Données

Les données générées peuvent être utilisées pour :
- L'analyse des établissements d'enseignement supérieur au Maroc
- La recherche et la comparaison des filières disponibles
- L'aide à la décision pour les futurs étudiants
- Des études statistiques sur l'enseignement supérieur

## Formats Disponibles

- JSON : Pour l'intégration dans des applications
- CSV : Pour l'analyse de données
- XLSX : Pour la visualisation et la manipulation manuelle 