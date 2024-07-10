# Allomovie

Ce projet comprend une application frontend Vue.js qui se connecte à un backend django (RestAPI) pour afficher et gérer des informations sur les films.

## Prérequis

Assurez-vous d'avoir Docker installé sur votre machine avant de continuer.

- Docker : [Installation de Docker](https://docs.docker.com/get-docker/)

## Installation et Utilisation

1. **Cloner le Repository**

   ```bash
   git clone https://github.com/jacquesbagui/allomovie
   cd allomovie

2. **Démarrer l'application**

    ```bash 
    make
    make migrate
    make init-test-data

- Application frontend accessible à: http://localhost:5173

- Application Backend accessible à: http://localhost:8000

- Application Backend Admin accessible à: http://localhost:8000/admin

3. **Création d'un Utilisateur Administrateur**

- Pour créer un utilisateur administrateur (superuser) dans votre backend Django :

  ```bash
  make createsuperuser

- Cette commande utilise :
   ```bash
    docker-compose run --rm backend python manage.py createsuperuser

4. **Arrêt des Services**

- Pour arrêter tous les services Docker :
  ```bash
  make down

## Commandes Utiles

- Logs en Temps Réel
    ```bash
    make logs
- Exécuter des Tests
    ```bash
    make test
## Configuration supplémentaire

- Pour ajuster les paramètres de développement ou d'environnement, veuillez consulter les fichiers docker-compose.yml, Dockerfile dans les répertoires backend et frontend.

## Notes:

- Assurez-vous que les ports **8000 (backend)** et **5173 (frontend)** ne sont pas déjà utilisés sur votre machine locale avant de démarrer les services Docker.
