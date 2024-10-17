# Smiley Generator Project - Clemaste

Bienvenue dans le projet Smiley Generator développé par le groupe Clemaste ! Ce projet permet de générer des smileys personnalisés en fonction des émotions perçues à travers un texte donné.

## Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributions](#contributions)
- [Contact](#contact)

## Présentation

Le projet Smiley Generator est une application Python où les utilisateurs peuvent générer des smileys basés sur différentes émotions. Grâce à une analyse du texte fourni, l'application détermine l'émotion prédominante et génère le smiley approprié.

**Groupe de développement : Clemaste**

- Clémentine : Back-End
- Matthieu : IA
- Stéphane : Front-End
- Manal : Front-End

## Fonctionnalités

- Génération de smileys via une interface web intuitive.
- Analyse de texte pour détecter les émotions à l'aide d'algorithmes d'intelligence artificielle.
- Frontend intégré utilisant le système de templates Django pour afficher les smileys générés.
- Possibilité de personnaliser les smileys en fonction des préférences des utilisateurs.

## Technologies Utilisées

- **Langage** : Python
- **Framework** : Django
- **Frontend** : HTML, CSS, JavaScript (avec Bootstrap pour le design responsive)
- **Base de données** : SQLite
- **Intelligence Artificielle** : Bibliothèques comme NLTK ou spaCy pour l'analyse de texte et la détection des émotions
- **Contrôle de version** : Git (avec GitHub pour le dépôt)

## Installation

### Prérequis

- Python 3.8+
- pip (Gestionnaire de paquets Python)
- Virtualenv (facultatif, pour isoler l'environnement)

### Étapes d'installation

1. Clonez le dépôt du projet :

    ```bash
    git clone https://github.com/clemaste/smiley_generator.git
    cd smiley_generator
    ```

2. (Facultatif) Créez un environnement virtuel :

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Sur Windows, utilisez .venv\Scripts\activate
    ```

3. Installez les dépendances nécessaires :

    ```bash
    pip install -r requirements.txt
    ```

4. Exécutez le serveur de développement Django :

    ```bash
    python manage.py runserver
    ```

5. Ouvrez votre navigateur et accédez à l'application à l'adresse suivante :

    ```
    http://localhost:8000/image-generator/
    ```

## Utilisation

- Entrez votre prompt dans le champ de texte prévu à cet effet.
- Cliquez sur le bouton "Generate" pour générer le smiley.
- L'image générée apparaîtra ci-dessus, avec la possibilité de l'enregistrer.

## Contributions

Les contributions au projet sont les bienvenues ! N'hésitez pas à soumettre des demandes de fonctionnalités ou à corriger des bogues en ouvrant des issues sur le dépôt GitHub.

## Contact

Pour toute question ou demande d'information, veuillez contacter les membres du groupe Clemaste via leur profil GitHub.

---

Merci d'avoir consulté le projet Smiley Generator ! Nous espérons que vous apprécierez l'utilisation de notre application.
