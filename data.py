import pandas as pd

# Dictionnaire des produits du magasin
magasin = {
    "produits": [
        {"nom": "Pain", "prix": 1.50, "categorie": "Alimentation"},
        {"nom": "Lait", "prix": 2.00, "categorie": "Alimentation"},
        {"nom": "Savon", "prix": 3.00, "categorie": "Hygiène"},
        {"nom": "Shampooing", "prix": 5.50, "categorie": "Hygiène"},
        {"nom": "Pomme", "prix": 0.80, "categorie": "Fruits"},
    ]
}

# Création d'un DataFrame
df = pd.DataFrame(magasin["produits"])

# Vérification
if __name__ == "__main__":
    print(df)

