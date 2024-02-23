<div align="center">

# Backend Template

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

---

French version of this : [README.fr.md](README.fr.md)
<a href="README.fr.md"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png" width="20" height="15" alt="French version"></a>

---

### **Description**

This is a highly secure backend template for a web application. It is designed to be used as a starting point for a new project. It is built with Python and FastAPI, and uses a PostgreSQL database. The authentication is handled with two JWT tokens, a refresh token and an access token.

---

[Installation and Execution](#installation) •
[Documentation](#documentation) •
[Contributions](#contributions)

</div>


## Main Features

- Highly secure
- Very fast
- Easy to add new features
- Easy to maintain
- RGPD compliant


## Table of Contents

- [Installation](#installation)
  - [Pre-requisites](#pre-requisites)
  - [Database Setup](#database-setup)
  - [Virtual environment](#virtual-environment)
- [Documentation](#documentation)
  - [Folder structure](#folder-structure)
- [Contributions](#contributions)
  - [Authors](#authors)
  - [Version control](#version-control)

# Installation
<sup>[(Back to top)](#table-of-contents)</sup>

## Pre-requisites
<sup>[(Back to top)](#table-of-contents)</sup>

Python 3.10.12 was used for this project.
PostgreSQL 16.1 was used for this project.

You can use this backend with this [frontend](https://github.com/alexdeloire/frontend-template).

## Database Setup
<sup>[(Back to top)](#table-of-contents)</sup>

Create a new database in PostgreSQL and run all of the SQL files in the `app/sql` folder.

Make sure to have a `.env` file in the root of the project with the following content:

```bash
POSTGRES_USER = 'your_user'
POSTGRES_PASSWORD = 'your_password'
POSTGRES_DB = 'your_db'
POSTGRES_HOST='your_host'
POSTGRES_PORT='your_port'
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
```

## Virtual environment
<sup>[(Back to top)](#table-of-contents)</sup>

Create virtual environment:

```bash
python3 -m venv env
```

Activate virtual environment (Linux):

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

# Documentation
<sup>[(Back to top)](#table-of-contents)</sup>

Comments provided throughout the code. Feel free to contact me for any questions.


## Folder structure
<sup>[(Back to top)](#table-of-contents)</sup>

The project is structured as follows:
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
<sup>[(Back to top)](#table-of-contents)</sup>

## Authors
<sup>[(Back to top)](#table-of-contents)</sup>

- [**Alexandre Deloire**](https://github.com/alexdeloire)
- [**Remi Jorge**](https://github.com/RemiJorge)

## Version control
<sup>[(Back to top)](#table-of-contents)</sup>

Git is used for version control.