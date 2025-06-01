import re
import json
import pandas as pd

# Lire le fichier texte brut
with open('DATASET-.txt', 'r', encoding='utf-8') as file:
    content = file.read().strip()

# Correction automatique des virgules manquantes entre les objets JSON
# Ajoute une virgule entre chaque } et { qui ne sont pas déjà séparés par une virgule
content = re.sub(r'}\s*{', '},\n{', content)

# Vérifie que le contenu commence par [ et finit par ]
if not (content.startswith('[') and content.endswith(']')):
    print("Le fichier ne contient pas un tableau JSON valide.")
    exit(1)

try:
    data = json.loads(content)
except Exception as e:
    print(f"Erreur lors du chargement du JSON : {e}")
    exit(1)

# Créer une nouvelle liste pour stocker les données dépliées
expanded_data = []

# Pour chaque entrée dans les données
for entry in data:
    # Séparer les villes
    villes = [v.strip() for v in entry.get('Ville', '').split(',')]
    
    # Récupérer et traiter les filières d'études possibles
    filieres = entry.get("Filières d'études possibles", [])
    
    # Si c'est une chaîne, essayer de la convertir en liste
    if isinstance(filieres, str):
        # Si c'est une chaîne JSON, essayer de la parser
        if filieres.strip().startswith('[') and filieres.strip().endswith(']'):
            try:
                filieres = json.loads(filieres)
            except:
                # Si le parsing échoue, traiter comme une chaîne normale
                filieres = [f.strip() for f in filieres.split(',')]
        else:
            # Traiter comme une chaîne normale
            filieres = [f.strip() for f in filieres.split(',')]
    
    # S'assurer que filieres est une liste
    if not isinstance(filieres, list):
        filieres = [str(filieres)]
    
    # Nettoyer les filières (enlever les crochets et les guillemets)
    filieres = [re.sub(r'[\[\]"]', '', str(f)).strip() for f in filieres]
    
    # Supprimer les entrées vides
    filieres = [f for f in filieres if f]
    
    # Si aucune filière n'est trouvée, ajouter une entrée vide
    if not filieres:
        filieres = ['']
    
    # Pour chaque combinaison ville-filière, créer une nouvelle entrée
    for ville in villes:
        for filiere in filieres:
            new_entry = entry.copy()
            new_entry['Ville'] = ville
            new_entry["Filières d'études possibles"] = filiere
            expanded_data.append(new_entry)

# Convertir en DataFrame
try:
    df = pd.DataFrame(expanded_data)
    print(f"Nombre total de lignes : {len(df)}")
    print("\nAperçu des premières lignes :")
    print(df[["Écoles/Instituts", "Ville", "Filières d'études possibles"]].head())
except Exception as e:
    print(f"Erreur lors de la conversion en DataFrame : {e}")
    exit(1)

# Sauvegarde en CSV avec encodage UTF-8-SIG pour Excel
try:
    df.to_csv('data_expanded.csv', index=False, encoding='utf-8-sig')
    print('\nFichier CSV créé avec succès !')
except Exception as e:
    print(f"Erreur lors de la sauvegarde CSV : {e}")

# Sauvegarde en Excel
try:
    df.to_excel('data_expanded.xlsx', index=False)
    print('Fichier Excel créé avec succès !')
except Exception as e:
    print(f"Erreur lors de la sauvegarde Excel : {e}") 