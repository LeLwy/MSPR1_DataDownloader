"""
config.py : Contient la configuration centrale du projet, comme les URLs des datasets
et les paramètres globaux.

Ce fichier permet de centraliser les paramètres et d'éviter les répétitions dans le code.
"""

# Liste des datasets à télécharger
DATASETS = [
    {
        "url": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-table-data.csv",  # URL du dataset
        "file_name": "global-data.csv"                                                                       # Nom du fichier local
    },
    {
        "url": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/vaccination-data.csv",
        "file_name": "vaccination-data.csv"
    },
    {
        "url": "https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/vaccination-metadata.csv",
        "file_name": "vaccination-metadata.csv"
    }
]

# Autres configurations potentielles (par exemple, fréquence de téléchargement)
DOWNLOAD_FOLDER = "downloads"  # Répertoire où les fichiers seront enregistrés
