<div align="center">

# Template Backend

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Ce travail est sous licence <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.

---

Version anglaise de ce document : [README.md](README.md)
<a href="README.md"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/1280px-Flag_of_the_United_Kingdom_%283-5%29.svg.png" width="20" height="15" alt="English version"></a>

---

### **Description**

Ce modèle de backend est conçu pour être utilisé comme point de départ pour un nouveau projet. Il est construit avec Python et FastAPI, et utilise une base de données PostgreSQL. L'authentification est gérée avec deux jetons JWT, un jeton de rafraîchissement et un jeton d'accès.

---

[Installation et Exécution](#installation) •
[Documentation](#documentation) •
[Contributions](#contributions)

**Veuillez lire attentivement la [Documentation](Documentation.pdf) fournie.**
</div>


## Fonctionnalités

- Très sécurisé
- Très rapide
- Facile à ajouter de nouvelles fonctionnalités
- Facile à maintenir
- Conforme au RGPD


## Table des matières

- [Installation](#installation)
  - [Prérequis](#prérequis)
  - [Setup de la base de données](#setup-de-la-base-de-données)
  - [Environnement Virtuel](#environnement-virtuel)
- [Documentation](#documentation)
  - [Structure du projet](#structure-du-projet)
- [Contributions](#contributions)
  - [Auteurs](#auteurs)
  - [Contrôle des versions](#contrôle-des-versions)

# Installation
<sup>[(Retour en haut)](#table-des-matières)</sup>

## Prérequis
<sup>[(Retour en haut)](#table-des-matières)</sup>

Python 3.10.12 a été utilisé pour ce projet.
PostgreSQL 16.1 a été utilisé pour ce projet.

Vous pouvez utiliser ce backend avec ce [frontend](https://github.com/alexdeloire/frontend-template).

## Setup de la base de données
<sup>[(Retour en haut)](#table-des-matières)</sup>

Créez une nouvelle base de données dans PostgreSQL et exécutez tous les fichiers SQL du dossier `app/sql`.

Assurez-vous d'avoir un fichier `.env` à la racine du projet avec le contenu suivant :

```bash
POSTGRES_USER = 'your_user'
POSTGRES_PASSWORD = 'your_password'
POSTGRES_DB = 'your_db'
POSTGRES_HOST='your_host'
POSTGRES_PORT='your_port'
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
```

## Environnement Virtuel
<sup>[(Retour en haut)](#table-des-matières)</sup>

Créer un environnement virtuel :

```bash
python3 -m venv env
```

Activer l'environnement virtuel (Linux):

```bash
source env/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

# Documentation
<sup>[(Retour en haut)](#table-des-matières)</sup>

Commentaires fournis tout au long du code. N'hésitez pas à me contacter pour toute question.

## Structure du projet
<sup>[(Retour en haut)](#table-des-matières)</sup>

Voici la structure du projet :

```bash
.
├── app
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── item_controller.py
│   │   └── user_controller.py
│   ├── database
│   │   ├── db.py
│   │   └── db_session.py
│   ├── models
│   │   ├── auth.py
│   │   ├── item.py
│   │   └── user.py
│   ├── routers
│   │   ├── auth_router.py
│   │   ├── items_router.py
│   │   └── user_router.py
│   └── sql
│       ├── auth.sql
│       └── items.sql
├── LICENSE.txt
├── main.py
├── README.fr.md
├── README.md
└── requirements.txt
```

# Contributions
<sup>[(Retour en haut)](#table-des-matières)</sup>

## Auteurs
<sup>[(Retour en haut)](#table-des-matières)</sup>

- [**Alexandre Deloire**](https://github.com/alexdeloire)
- [**Remi Jorge**](https://github.com/RemiJorge)

## Contrôle des versions
<sup>[(Retour en haut)](#table-des-matières)</sup>

Git est utilisé pour le contrôle des versions.
