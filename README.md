---
marp: true
size: A4
paginate: true
header: 'PROJET — Documentation Technique'
footer: 'Page %PAGE%'
style: |
  section {
    width: 210mm;
    height: 297mm;
    padding: 25mm 20mm;
    font-size: 13pt;
    line-height: 1.5;
    justify-content: flex-start;
  }
  h1 { color: #0f172a; border-bottom: 2px solid #0ea5e9; padding-bottom: 8px; font-size: 22pt; }
  h2 { color: #1e293b; margin-top: 25px; font-size: 16pt; }
  h3 { color: #0ea5e9; margin-top: 15px; font-size: 13pt; }
  code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-size: 11pt; }
  ul { line-height: 1.6; }
---

# Automatisation de Workflow & Gestion d'Agent IA

Ce projet a été conçu pour apprendre l'automatisation de workflow et la gestion d'agent IA en utilisant le framework **aider**.

---

## Architecture du Projet

L'architecture du projet est basée sur le modèle de **Clean Architecture**, avec une séparation stricte des responsabilités.

### Couche d'Infrastructure
- `auth/repository/auth_repository.py` : Logique de base de données pour l'authentification.

### Couche de Domaine
- `auth/service/auth_service.py` : Logique métier liée à l'authentification.

### Couche de Contrôleurs
- `auth/controller/auth_controller.py` : Gestion des requêtes d'authentification.

---

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