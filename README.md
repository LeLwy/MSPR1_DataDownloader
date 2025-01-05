# COVID Data Downloader and Scheduler

Une application Python permettant de télécharger des datasets COVID-19 depuis des URLs fournies, de les sauvegarder dans un répertoire spécifique, et de planifier des téléchargements hebdomadaires. Le projet comprend un processus d'extraction de données ETL (Extract, Transform, Load) et la planification de l'exécution régulière des tâches.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Exécution](#exécution)
- [Planification](#planification)
- [Fonctionnalités](#fonctionnalités)

## Prérequis

Avant de commencer, vous devez vous assurer que votre environnement Python contient toutes les dépendances nécessaires. Ce projet utilise les bibliothèques suivantes :

- `requests` : pour télécharger les fichiers CSV à partir des URLs.
- `schedule` : pour planifier l'exécution des téléchargements hebdomadaires.

## Installation

### Étape 1 : Clonez le projet
Si vous n'avez pas encore cloné le projet, utilisez la commande suivante :
```bash
git clone https://votre-lien-repository.git
```

### Étape 2 : Créez un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet :
```bash
python3 -m venv venv
```

### Étape 3 : Activez l'environnement virtuel

- Sur Windows:
```bash
venv\Scripts\activate
```

- Sur macOS/Linux:
```bash
source venv/bin/activate
```

### Étape 4 : Installer les dépendances

Une fois l'environnement virtuel activé, installez les bibliothèques nécessaires en utilisant `requirements.txt` :
```bash
pip install -r requirements.txt
```

## Configuration

Avant d'exécuter l'application, vous devez définir les datasets à télécharger dans le fichier `config.py` :

### Format du fichier `config.py`
```bash
DATASETS = [
    {
        "url": "https://example.com/covid-dataset-1.csv",
        "file_name": "covid_dataset_1.csv"
    },
    {
        "url": "https://example.com/covid-dataset-2.csv",
        "file_name": "covid_dataset_2.csv"
    }
]
```
- url : URL du fichier CSV à télécharger.
- file_name : Nom du fichier sous lequel il sera enregistré localement dans le répertoire `downloads`.

### Répertoire de téléchargement

Les fichiers seront enregistrés dans un répertoire appelé `downloads`. Ce répertoire sera créé automatiquement s'il n'existe pas déjà.

Si vous souhaitez modifier le répertoire de téléchargement, vous pouvez ajuster la variable `DOWNLOAD_FOLDER` dans `config.py`.

## Exécution

### Étape 1 : Télécharger les fichiers immédiatement

Une fois la configuration terminée, vous pouvez télécharger les fichiers immédiatement en exécutant :
```bash
python main.py
```
Cela téléchargera tous les datasets définis dans `config.py` et les enregistrera dans le répertoire `downloads`.

### Étape 2 : Planifier les téléchargements hebdomadaires

L'application utilise la bibliothèque `schedule` pour planifier des téléchargements réguliers tous les sept jours. Les tâches sont automatiquement planifiées lors de l'exécution de `main.py`.

### Étape 3 : Garder le planificateur en cours d'exécution

Après avoir exécuté le script `main.py`, le planificateur reste actif et exécute automatiquement les téléchargements toutes les semaines.

## Planification

L'application utilise la bibliothèque `schedule` pour effectuer des téléchargements hebdomadaires. Vous pouvez configurer cette planification directement dans le fichier `scheduler.py`.

Le planificateur vérifie les URLs définies dans `config.py` et déclenche le téléchargement tous les 7 jours.

## Fonctionnalités

- Téléchargement de datasets : Téléchargez les fichiers CSV à partir des URLs définies dans config.py.
- Planification des téléchargements : Planifiez des téléchargements hebdomadaires via la bibliothèque schedule.
- Gestion automatique du répertoire : Le répertoire downloads est créé automatiquement s'il n'existe pas.
- Gestion des erreurs : Si un fichier ne peut pas être téléchargé, le programme affiche un message d'erreur sans interrompre l'exécution des autres tâches.