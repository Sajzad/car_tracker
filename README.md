# Car-Tracker
This README would normally document whatever steps are necessary to get your application up and running.

### Tech. used in the porject? ###

* DRF
* python >=3.6
* Django
* Vue Js

### How do I get set up? ###

* Please Clone the repo: ```git clone https://github.com/Sajzad/car_tracker.git```.

* Install virtualenv on your system. For linux: ```pip install virtualenv```.

* Now, we go to car_tracker dir. And create virtual environment with virtualenv: ```virtualenv -p /usr/bin/python3 .env```.

* Activate the virtual environment: source ```.env/bin/activate```.

* Install required dependencies: ```pip install -r requirements.txt```.

* For the development server, environment variable may interrupt crontab, to solve it requires few extra steps. so to reduce the hassle, 	I would prefer hard coded values in the development server.

* Go to website dir where the manage.py file.

* Create migrations files: ```./manage.py makemigrations```.

* Update the database with migrations: ```./manage.py migrate```.

* Update the database with migrations: ```./manage.py crontab add```.

* Start the local server: ```./manage.py runserver```.

* Server can be accessed from this link ```http://127.0.0.1:8000/```.

### How do I get set up PostGreSQL? ###
1. First install DB and necessary packages
```
sudo apt update
```
```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```
2. Install the adaptor 
```pip install psycopg2-binary``` 
3. Now, we are going to jump right into Create Datebase and User. 
```sudo -u postgres psql``` 
```CREATE DATABASE myproject;``` 
```
USER myprojectuser WITH PASSWORD 'password';
```
```
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
```
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

```
Now we are finished. We will set db_name, user and password in the settings.py. Now we can quit the prompt typing  ```\q```
