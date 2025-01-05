import os
import requests

def download_file(url, file_name="covid_data.csv"):
    """
    Télécharge un fichier à partir d'une URL et le sauvegarde dans un répertoire local.

    Arguments :
    ----------
    url : str
        L'URL du fichier à télécharger. Cette URL doit pointer directement vers un fichier.
    file_name : str, optionnel
        Le nom sous lequel le fichier sera sauvegardé dans le répertoire local (par défaut "covid_data.csv").

    Fonctionnement :
    ----------------
    1. Vérifie si un répertoire pour les téléchargements existe (par défaut "downloads").
       Si le répertoire n'existe pas, il est créé automatiquement.
    2. Vérifie si un fichier portant le même nom existe déjà dans ce répertoire :
       - Si oui, un message d'avertissement est affiché (le fichier sera écrasé).
    3. Télécharge le fichier depuis l'URL donnée en utilisant la bibliothèque `requests`.
       - Si une erreur HTTP se produit (URL invalide, serveur indisponible, etc.), un message d'erreur est affiché.
    4. Sauvegarde le fichier en le téléchargeant par morceaux (chunks) pour économiser la mémoire.
    5. Affiche un message de succès une fois le téléchargement terminé.

    Exceptions :
    ------------
    - Les erreurs de réseau ou HTTP sont interceptées et affichées sous forme de messages lisibles.

    Exemple d'utilisation :
    -----------------------
    download_file("https://example.com/file.csv", "dataset.csv")
    """
    # Nom du dossier où les fichiers seront téléchargés
    DOWNLOAD_FOLDER = "downloads"

    # Crée le dossier s'il n'existe pas déjà
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    try:
        # Vérifie si le fichier existe déjà dans le dossier
        if os.path.exists(file_path):
            print(f"Attention : Un fichier existant a été détecté à l'emplacement {file_path}. Il sera écrasé.")

        # Affiche un message pour indiquer le début du téléchargement
        print(f"Téléchargement du fichier depuis l'URL : {url}")

        # Envoie une requête GET pour télécharger le fichier
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Soulève une exception si la requête échoue

        # Ouvre le fichier en mode binaire et écrit les données téléchargées par morceaux
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        # Affiche un message de confirmation une fois le téléchargement terminé
        print(f"Téléchargement réussi : Le fichier a été sauvegardé à l'emplacement {file_path}")
    except requests.exceptions.RequestException as e:
        # Gère toutes les erreurs liées au téléchargement (ex. : réseau, URL incorrecte)
        print(f"Erreur lors du téléchargement : {e}")