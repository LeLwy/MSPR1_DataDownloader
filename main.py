"""
main.py : Point d'entrée principal du projet.

Ce fichier combine les différentes fonctionnalités du projet :
1. Télécharge les fichiers immédiatement (pour garantir une première mise à jour).
2. Planifie les téléchargements hebdomadaires.
3. Maintient le planificateur actif.
"""

import time
from downloader.downloader import download_file
from downloader.scheduler import schedule_download, run_scheduler
from config.config import DATASETS

def initialize_downloads():
    """
    Télécharge immédiatement tous les fichiers définis dans la configuration.

    Fonctionnement :
    ----------------
    - Parcourt la liste des datasets définis dans `config.DATASETS`.
    - Télécharge chaque fichier une fois avant de commencer la planification.
    """
    print("Initialisation : Téléchargement immédiat de tous les datasets.")
    for dataset in DATASETS:
        download_file(dataset["url"], dataset["file_name"])

def schedule_all_downloads():
    """
    Planifie les téléchargements hebdomadaires pour tous les datasets.

    Fonctionnement :
    ----------------
    - Parcourt la liste des datasets définis dans `config.DATASETS`.
    - Crée une tâche planifiée pour chaque fichier à l'aide de `schedule_download`.
    """
    print("Planification des tâches hebdomadaires...")
    for dataset in DATASETS:
        schedule_download(dataset["url"], dataset["file_name"])

if __name__ == "__main__":
    """
    Point d'entrée principal du projet.

    Fonctionnement :
    ----------------
    1. Télécharge immédiatement tous les fichiers pour garantir une mise à jour initiale.
    2. Planifie les tâches hebdomadaires pour tous les datasets.
    3. Lance le planificateur pour surveiller les tâches futures.
    """
    try:
        print("=== Lancement du Projet ===")
        initialize_downloads()      # Étape 1 : Téléchargement initial
        schedule_all_downloads()    # Étape 2 : Planification des tâches
        run_scheduler()             # Étape 3 : Lancement du planificateur
    except Exception as e:
        print(f"Erreur critique : {e}")
