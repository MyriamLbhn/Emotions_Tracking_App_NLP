
# Emotions Tracking Application

## Objectifs 

Ce site est à destination de psychologues et leurs patients.  
Les psychologues peuvent :
- avoir accès à un espace de connexion particulier pour y visualiser la répartition des émotions de leurs patients actifs sur une certaine période de temps.
- visualiser la répartition des émotions d’un de leur patients en recherchant par son nom et prénom.
- rechercher tous les textes contenant une certaines expressions.
- créer un nouveau patient avec un mot de passe par défaut, un nom et un prénom.

Les patients peuvent :
- accéder à un espace privé de connexion.
- créer un nouveau texte.

Les textes écrits par les patients soient automatiquement évalués par un modèle hugging face déployé sur le hub.
Les informations sur les patients et psychologues doivent être enregistrées dans une base postgres.  
Les textes et les évaluations dans une base elastic search.   

## Installation

1. Créer les fichiers .env avec les informations suivantes : 
```
POSTGRES_DB=au_choix
POSTGRES_USER=nom_utilisateur_au_choix
POSTGRES_PASSWORD=mdp_au_choix
POSTGRES_NAME=nom_bdd_au_choix
DB_HOST=db

SECRET_KEY = 'votre_secret_key_django'
DEBUG = True
```

2. `docker build -t emotiontracking .` pour consuitre l'image 

3. `docker compose up`  pour démarrer les conteneurs définie dans le fichier *docker-compose.yml*

4. On a maintenant accès à :
- l'application Django : http://localhost:8000/
- la bdd postgresql (avec adminer) : http://localhost:8080/
- la bdd ElasticSearch : http://localhost:9200/

5. Pour ouvrir le shell du conteneur django : `docker compose exec web bash`

6. Depuis ce shell, vous pouvez créer un superuser si vous le souhaitez : `python manage.py createsuperuser`

6. Il faut maintenant créer au moins 1 compte en tant que psychologue (depuis le shell, le portail admin ou depuis http://localhost:8000/register/)

8. Pour remplir nos bdd, executer les fichiers suivants dans le shell du conteneur django : 
- `python utils/random_patient.py`: crée x patients (vous pouvez modifier ce nombre directement dans le fichier python, en argument de la fonction)
- `./command/mapping.sh`pour créer l'index note 
- `python utils/populate_index.py` pour créer x document (vous pouvez modifier ce nombre directement dans le fichier python, en argument de la fonction)

9. Vous pouvez maintenant naviguer sur l'application et accéder à toutes ses fonctionnalités.


## Requirements

Installez les bibliothèques requises à l'aide de `pip install -r requirements.txt` ou installez-les manuellement.


## Crédits
Le modèle utilisé pour l'évaluation des textes a été entraîné, fine-tuné et déployé par Michelle Jieli. Vous pouvez trouver le modèle sur le hub Hugging Face à l'adresse suivante : https://huggingface.co/michellejieli/emotion_text_classifier