# Automatisation de Workflow & Gestion d'Agent IA

Ce projet a été conçu pour apprendre l'automatisation de workflow et la gestion d'agent IA en utilisant le framework **aider**.

## Architecture du Projet

L'architecture du projet est basée sur le modèle de **Clean Architecture**, avec une séparation stricte des responsabilités.

### Couche d'Infrastructure
- `auth/repository/auth_repository.py` : Logique de base de données pour l'authentification.

### Couche de Domaine
- `auth/service/auth_service.py` : Logique métier liée à l'authentification.

### Couche de Contrôleurs
- `auth/controller/auth_controller.py` : Gestion des requêtes d'authentification.

## Tests Unitaires

Les tests unitaires sont écrits pour chaque nouvelle fonction dans les fichiers suivants :

- `auth/tests/test_auth_repository.py`
- `auth/tests/test_auth_service.py`
- `auth/tests/test_auth_controller.py`

## Conventions de Nommage

- **Variables & Fonctions** : `snake_case` (Python/Backend)
- **Classes & Interfaces** : `PascalCase`
- **Fichiers** : `snake_case` ou `kebab-case`

## Modélisation des Rôles d'Agents

- **Dev** : Génère du code modulaire avec gestion d'erreurs explicite.
- **Test** : Écrit des tests unitaires isolés pour chaque nouvelle fonction.
- **Doc** : Ajoute des docstrings au format Google/Sphinx et met à jour le `README.md`.