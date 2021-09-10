
# Application Chessy

## Description

L'application Chessy permet de gérer un tournoi d'échecs suivant le **système suisse**.

Chaque tournoi accueillera 8 joueurs et sera composé de 4 tours, chacun comptant 4 matchs.

La génération des paires de joueurs pour chaque match se fait automatiquement, ainsi que la mise à jour des scores.

L'application permet également de gérer une liste de joueurs inscrits et de modifier leur classement ELO respectif.

## Configuration requise

[Python **3.9.6**](https://www.python.org/downloads/release/python-396/)

Un navigateur internet (*exemple* : [Chrome](https://www.google.com/chrome/)) pour ouvrir le rapport flake 8.

Une connexion internet n'est pas requise.

## Installation et configuration

1. **Activer l'environnement virtuel**

    * Depuis la console, se positionner dans le dossier de l'application à l'aide de la commande 'cd'.

    *Exemple* :

    `C:\Users\<UserName>>cd Desktop\Chessy`

    `C:\Users\<UserName>\Desktop\Chessy>`

    * Activer l'environnement virtuel avec la commande correspondant au Système d'exploitation.

    *Windows* :

    `env\Scripts\activate.bat`

    *Unix ou Mac* :

    `source env/Scripts/activate`

    **Ces actions seront à effectuer avant chaque lancement de l'application.**

2. **Installer le fichier requirements.txt**

    Entrer la commande suivante depuis le dossier de l'application :

    `pip install -r requirements.txt`

3. **Lancer l'application**

    Depuis la console, entrer la commande suivante :

    `py main.py`

    Le menu principal s'affiche alors.

## Utilisation

Une fois l'application lancée, il suffit de presser la touche correspondant à l'action souhaitée.

*Exemple* :

```cmd
-------------------------
Bienvenue dans l'application Chessy !
-------------------------


1: Lancer un nouveau tournoi
2: Reprendre un tournoi
3: Afficher les rapports des joueurs
4: Afficher les rapports des tournois
5: Changer le classement Elo d'un joueur
6: Quitter
Entrez votre choix  : 1
```

```cmd
Entrez le nom du tournoi :
```

Pour créer un **nouveau tournoi**, il faut renseigner :

* un nom
* un lieu
* une date (format jj/mm/aaaa)
* un type de contrôle de temps (bullet, blitz ou rapide).

Il est aussi possible de renseigner une description du tournoi.

Pour créer un **nouveau joueur**, il faut renseigner :

* un nom de famille
* un prénom
* une date de naissance (format jj/mm/aaaa)
* un sexe (f ou m)
* un classement ELO

Lors de la création d'un nouveau tournoi, on peut au choix ajouter un nouveau joueur ou choisir un joueur existant dans la base de données. La recherche se fait par prénom, et l'on peut choisir le joueur souhaité dans la liste qui s'affiche.
Un nouveau joueur est automatiquement ajouté à la base de données.
Un même joueur (même nom, même prénom, même classement) ne peut être ajouté 2 fois à la base de données.

On peut revenir au menu principal après chaque tour.

Il est possible de modifier le classement ELO des joueurs à la fin d'un tournoi ou depuis le menu principal.

L'application permet également d'afficher différentes données concernant les joueurs ou les tournois.

## Générer un rapport flake 8

Afin de vérifier que le code de l'application correspond bien aux normes du langage Python, il est possible de générer un rapport flake 8 au format html avec la commande suivante :

`flake8 --format=hmtl --htmldir=flake-report`

Il suffit alors d'ouvrir le fichier <index.html> créé dans le dossier flake-report. Pour générer le fichier dans un autre dossier, il faudra renseigner le nom du dossier après la commande "htmldir=".
