# DataManager

![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-positive.png)

# Data Manager App:

Data Manager Application as a Back-end software for Strades. This app is used to manage the data that is collected from the Stradeso's Data Collector App. The Data Manager App is used to create, read, update, and delete data from the database. The app is also used to create and manage users and their permissions.

This repository contains a simple Django app as part of the **Deploying a Production ready Django App on EC2 with CI/CD** gist tutorial which you can find [here](https://gist.github.com/rmiyazaki6499/92a7dc283e160333defbae97447c5a83)

## Table of Contents:

- [Project Layout](#project-layout)
- [Requirements](#requirements)
- [Setting up the Django-app project with Docker](#setting-up-the-django-app-project-with-docker)
  - [Install Docker](#install-docker)
  - [Build and Run the Container](#build-and-run-the-container)
  - [Cleaning up the Container and Image](#cleaning-up-the-container-and-image)
- [Setting up the Django-app project manually](#setting-up-the-django-app-project-manually)
- [Authors](#authors)

## Project Layout:

```
DATAMANAGER/
  |___ backend/ (Django Backend settings)
  |   |___ settings.py
  |___ static_files/
  |___ templates/ (Django Templates)
  |   |___ index.html
  |___ scripts/
  |___ manage.py
  |___ requirements.txt
  |___ Dockerfile
  |___ docker-compose.yml

```

The default settings are typically built for development rather than production and I found it difficult to change my settings after building the project. My inspiration comes from this article here: https://djangostars.com/blog/configuring-django-settings-best-practices/ where the different approaches are listed. 

My approach uses the **django-environ** package (https://django-environ.readthedocs.io/en/latest/#) which makes it relatively easy to manage your development and production environment variables.

I have also included the **django-debug-toolbar** (https://django-debug-toolbar.readthedocs.io/en/latest/) which I found useful in debugging and optimizing Django, specifically when it came to how my app queries the database.

**Note: Make sure to add the .env files to your .gitignore. They are not included by default in this project so that you have a reference to what type of data should be in there.**

## Requirements

- Python 3.9+
- Django 4.0+

## Setting up the Django-Scrapper-app project with Docker

For those that are not interested in setting up the project manually or would simply not have to worry about downloading python and its dependencies, I have created a Dockerfile and docker-compose.yml file to help create a container with everything you would need to run the **django-scrapper-app**.

### Install Docker

To make this as easy as possible, we will be using *Docker Compose* to creat our container.

- If you do not have Docker yet, start by downloading it if you are on a Mac or Windows:
https://www.docker.com/products/docker-desktop

- Or if you are on a Linux Distribution follow the directions here:
https://docs.docker.com/compose/install/

- To confirm you have Docker Compose, open up your terminal and run the command below:

```
$ docker-compose --version
Docker Compose version v2.18.1
```

### Build and Run the Container

- Clone the repo to your local machine:

```
$ git clone https://github.com/rmiyazaki6499/django-app.git
```

- Go into the project directory to build and run the container with:

```
$ cd django-app/
$ docker-compose up --build
```

Navigate to http://localhost:8000 to view the site on the local server.
It should look something like this:

![django-default](https://user-images.githubusercontent.com/41876764/87993902-8d27df00-caa0-11ea-8f66-990932b37ca3.png)

### Cleaning up the Container and Image

To stop the container from running, use `<Ctrl-C>` twice.
To close down the container use the command:

```
$ docker-compose down
```
Then to clean up the container and image which we are no longer using use the command:

```
$ docker system prune -fa
```

Confirm that the container and image is no longer there with:

```
$ docker system df -v
```

## Setting up the Django-app project manually

If you either did not want to use Docker or was curious to build the `django-app` manually follow the directions below.

- On your terminal and clone the repository with Git:

```
$ git clone https://github.com/rmiyazaki6499/django-app.git
```

- Next, go into the project directory and make sure you create a virtual environment for your project by either using venv or pipenv:
```
$ cd django-app/
$ python3 -m venv env
$ source env/bin/activate
```

- In order to install Python dependencies, make sure you have pip (https://pip.pypa.io/en/stable/installing/)
and run this command from the root of the repo:

```
$ pip3 install -r requirements.txt
```

- We will now migrate the database and collect the static files:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

- To run the development server, use the following command:

```
$ python3 manage.py runserver
```

- To run the production server, use the following command:

```
$ ENV_PATH=.env-prod python3 manage.py runserver
```

Navigate to http://localhost:8000 to view the site on the local server.
It should look something like this:

![django-default](https://user-images.githubusercontent.com/41876764/87993902-8d27df00-caa0-11ea-8f66-990932b37ca3.png)



<h3> version 0.0.0 </h3>

### Steps:

- Scrap data from the web or API from Sources.json on schedule
- Store Raw data in 'RAWSOURCES' Databases
- Gather data from each categories
- Check, clean, mix and format Data
- Stock the formatted data into relevant databases
- Extract data relevant data to views or test

--------------
### How to Run the software:

- Docker-compose up on AWS or OVH


-------------------
## views:
**- Web Dashboard**
Main categories:

    Overall Data: 
    - Selection/Notations : news, markets, reports documentations, statistics, states
    Trades:
    - Defintions : relations, tactics, strategies, agenda, plannings
    Results:
    - Decisions : Bots, Wallets, performances
    Community:
    - Communications: Shop, messages, contacts, events, organizations


**- 4D Relational Databases visualization**
show relations between data and trades in a 3D space
Can select specific planes of data to be highlighed

**- Scheduler -**
show past/present/future events
manage the time of executions

**- Settings-**
show software informations
manage user setup

**- Components-**
```
    - navbar:
        - logo/home button
        - 
    - toolbar:
       - search bar
       - connect button
```
écran principal:
Titre / bouton "start" / vérification du profil.

écran de connexion au profil:
Nom + mode de passe / s'inscrire / rester connecté.

écran de choix des mouvements boursiers:
liste des actifs financiers au jour j / choix de l'utilisateur.

- Results :
results of the algorithms and of the user's wallet of each asset.

- Historic :
calendar of assets / retrosprection of the results against the algorithm.

---------------------------

------------------------------------

## Design of the software:
**Database.py**:
execute SQL scripts to deal with the PostgreSQL databases 


**Dataminer.py**:
Récupère les données depuis le web.
Scrapping or API
Gère les Protocols de Scrapping propres à chaque Source

**Datamanager.py**:
Master the exchange of informations from all the sources
Manage the relation between info extracted by Dataminer.py and their storage in Database.py
Manage the agenda of executions
Clean and check up the data info from Dataminer.py



**Predictor.py**:
Produce current and future data for the views
Check the quality of the data created and return the result
It helps to always show relevants overall data

**Ingestion.py**:
Responsible for loading historical data.
Streaming real time data (prices,quotes,trades,etc.)
map and sanitize the data into standardized format
Also Feed data to the view Dashboard

**Strategy.py**:
hooks into Ingestion.py using events such as 'OnTrade','OnAggregateBar',etc.
Multiple independent strategies can be registered and run.
Feeding strategies interfaces with events makes BacktestEngine run on same code than the live trading processor.

--Classes:--
```
    - class events()
    - class eventChain()
    - class strategies()
    - class analysis()
    - class tradingDecisions()
    - class sanitizer()
    - class mapper()
```
**Brokerage.py**:
Strategies -> Brokerage -> Manage Money Positions
Interact with Brokerage

place and monitors trades from strategies
Execute the trades between the differents wallets and the trading plateforms
Produce an overall tradingContext report presenting the current state.
It is accessed from a lot of differents places by the code and used to get informations.
```
- class portfolio
(
    info:
        from brokerage account,
        pending trades,
        open positions,
        history of the session
)
```

--------------------------------------------------


-------------------------------------------------------------------------
## Web Server:

NGINX
Docker container (kubernetes) 
Tor

## Software Tools:

##### Python Librairies:
- Pandas
- Numpy
- Matplotlib
- Scikit-learn
- Tensorflow
- Django 4.0
- Selenium 4 / Scrappy / BeautifulSoup

##### Container:
- Linux Ubuntu 17

##### OSs: 
- Windows 10, MacOS M1, Linux

### Cloud Services:

- Github
- AWS
- OVH

##### API services:
```
- ChatGPT(article generation)
- Auth0 (for authentification) 
- Twilio (for sending text messages)
```

------------------------------------------------------------------------------------------

## Architecture of the Relational Databases:

#### PostgreSQL

**USER_LOGGING_INFO**:
> | UserID (PK) | Pseudo | Email | DateCreationAccount | CountryCode | Address | Name | Surname | LastConnection | 

**USER_LOG_INFO**:
> | Pseudo | Email | DateCreationAccount | CountryCode | Address | Name | Surname | LastConnection | ID_account | AvgConnectionTime | nbConnections |

**DB_LIVE_SCRAPPER_LOGS_INFO**:

**DB_HISTORICAL_PRICES_STORAGE**:

**DB_PROTOCOLS_STORAGE**:

Tables:
| id | timeGMT | SoftwareVersion | ActionChain |
Garde l'ordre et le temps dans lesquels ce programme "Scrapper" a opéré ses diverses fonctions. 

**DB_EVENTS**:
| IdEvent (PK)| UserID (FK)| PlatformID (FK)| EventTypeID (FK) | Value | Timestamp |

**EventTypes**:
| EventTypeID (PK) | EventName (status update, group created, friend added, friend removed, video posted, image posted, etc...) |

**Platforms**:
| PlatformID (PK) | PlatformName (Facebook, Youtube, likedin, etc) |

---------------------------------------------------------------------------------------------------

## Author

Created by:

- [Maximilien Pelletier](https://github.com/AceOfStrades)