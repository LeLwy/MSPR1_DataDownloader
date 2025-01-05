import schedule
import time
from downloader.downloader import download_file

def schedule_download(url, file_name="covid_data.csv"):
    """
    Planifie une tâche de téléchargement hebdomadaire pour un fichier spécifique.

    Arguments :
    ----------
    url : str
        L'URL du fichier à télécharger. Cette URL doit pointer directement vers un fichier.
    file_name : str, optionnel
        Le nom sous lequel le fichier sera sauvegardé dans le répertoire local (par défaut "covid_data.csv").

    Fonctionnement :
    ----------------
    1. Utilise la bibliothèque `schedule` pour planifier une tâche qui exécute la fonction `download_file`.
       - Par défaut, la tâche est configurée pour s'exécuter une fois par semaine.
    2. Le téléchargement utilise la même logique que celle définie dans `downloader.py`.

    Exemple d'utilisation :
    -----------------------
    schedule_download("https://example.com/dataset.csv", "my_dataset.csv")
    """
    # Planifie l'exécution de la fonction `download_file` chaque semaine
    schedule.every().week.do(download_file, url, file_name)
    print(f"Tâche planifiée : téléchargement hebdomadaire de {file_name} depuis {url}.")


def run_scheduler():
    """
    Démarre et maintient le planificateur en exécution continue.

    Fonctionnement :
    ----------------
    1. Vérifie périodiquement (toutes les 60 secondes) s'il existe une tâche planifiée prête à être exécutée.
    2. Utilise la bibliothèque `schedule` pour gérer les tâches.
    3. Permet au programme de rester actif pour exécuter les tâches futures.

    Remarque :
    ----------
    Cette fonction est bloquante. Si vous l'appelez, le script restera en exécution 
    jusqu'à ce qu'il soit arrêté manuellement.

    Exemple d'utilisation :
    -----------------------
    run_scheduler()
    """
    print("Planificateur lancé : en attente des tâches planifiées...")

    try:
        while True:
            # Exécute toutes les tâches planifiées prêtes à l'exécution
            schedule.run_pending()
            
            # Attend 60 secondes avant de vérifier à nouveau
            time.sleep(60)
    except KeyboardInterrupt:
        # Permet de gérer un arrêt manuel du programme (Ctrl + C)
        print("Planificateur arrêté par l'utilisateur.")
