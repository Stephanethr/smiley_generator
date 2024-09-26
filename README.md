# Projet : BiblioManager

## Objectif :
Créer un programme qui gère une bibliothèque de livres, permettant à un utilisateur de gérer un catalogue de livres, suivre les emprunts et retours, ainsi que la recherche dans la base de données.

## Fonctionnalités :

- **Ajout de livres :**
    - Permettre l’ajout d’un nouveau livre dans le système avec des informations comme le titre, l’auteur, l’année de publication, le genre, etc.

- **Recherche de livres :**
    - Offrir une fonctionnalité de recherche selon différents critères (titre, auteur, genre, année de publication).

- **Gestion des emprunts et retours :**
    - Suivre les livres empruntés par les utilisateurs.
    - Gérer les retours, avec un système de date d’échéance et des pénalités si le livre est rendu en retard.

- **Affichage du catalogue :**
    - Afficher tous les livres disponibles dans la bibliothèque, triés selon différents critères (par titre, auteur, année, etc.).

- **Système de sauvegarde :**
    - Sauvegarder l’état actuel de la bibliothèque dans un fichier pour garder les données même après la fermeture du programme.

- **Gestion des utilisateurs :**
    - Ajouter la possibilité de créer des comptes utilisateurs pour suivre quel livre a été emprunté par quel utilisateur.

## Technologies utilisées :

- **Fichiers texte** pour la sauvegarde et le chargement des données (livres, emprunts, utilisateurs).
- **STL (Standard Template Library)** pour gérer les listes et les recherches (utilisation de `std::vector`, `std::map`, etc.).
- **Classes et objets** pour représenter les livres, utilisateurs, emprunts.

## Extension possible :

- Ajouter une interface graphique avec une bibliothèque comme **Qt** ou **SFML** pour rendre l’application plus conviviale.
