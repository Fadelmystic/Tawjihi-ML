# Guide Tawjihi Data Analysis

Ce projet vise à analyser et nettoyer les données du guide Tawjihi pour les établissements d'enseignement supérieur au Maroc.

## Structure du Projet

```
.
├── Tawjihi ML/
│   ├── TAWJIHI-ML-Analysis.ipynb    # Notebook d'analyse principal
│   ├── clean_thresholds.py          # Script de nettoyage des seuils
│   ├── data_expanded.csv           # Données brutes
│   ├── data_expanded_cleaned.csv   # Données nettoyées (CSV)
│   ├── data_expanded_cleaned.xlsx  # Données nettoyées (Excel)
│   └── threshold_analysis.png      # Visualisation des seuils
└── README.md
```

## Fonctionnalités

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

3. **Formats de Sortie**
   - CSV : Format brut pour l'analyse
   - Excel : Format enrichi avec statistiques par type d'établissement et par ville
   - PNG : Visualisations des seuils

## Utilisation

1. **Installation des Dépendances**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
   ```

2. **Exécution du Nettoyage**
   ```bash
   python clean_thresholds.py
   ```

3. **Analyse Interactive**
   - Ouvrir `TAWJIHI-ML-Analysis.ipynb` dans Jupyter Notebook
   - Exécuter les cellules pour l'analyse interactive

## Résultats

Le script génère trois fichiers principaux :
1. `data_expanded_cleaned.csv` : Données nettoyées au format CSV
2. `data_expanded_cleaned.xlsx` : Données enrichies avec statistiques au format Excel
3. `threshold_analysis.png` : Visualisation des distributions des seuils

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 