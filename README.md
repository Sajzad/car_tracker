# Car-Tracker
This README would normally document whatever steps are necessary to get your application up and running.

### Tech. used in the porject? ###
* python >=3.6
* Javascript
* Django Rest Framework
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

* Now we will initiate the crontab: ```./manage.py crontab add```. Type ```crontab -e``` to check cronjob is added right away.

* We will create a superuser who is actually a manager for the system. Please type ```./manage.py createsuperuser``` and follow the shown process.

* Start the local server: ```./manage.py runserver```.

* Server can be accessed from this link ```http://127.0.0.1:8000/```.

* If you want superuser/manager access please go ```http://127.0.0.1:8000/admin```.

### How do I get set up PostGreSQL? ###

1. First install DB and necessary packages
```
sudo apt update
```
```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```
2. Install the adaptor 


```
pip install psycopg2-binary
``` 
3. Now, we are going to jump right in Creating Database and User.


```
sudo -u postgres psql
``` 
```
CREATE DATABASE myproject;
``` 
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
Now we are finished. We will set db_name, user and password in the settings.py. We can quit the prompt typing  ```\q```

# Frontend with snapshots

### Manager Dashboard ###

1. First let's access as a superuser/manager from this link .```http://127.0.0.1:8000/admin``` and then ```http://127.0.0.1:8000/``` .Side menu has the all modules.


![dashboard-managers](https://user-images.githubusercontent.com/42478821/150470840-7c0bb2e5-e336-4da1-9e1b-09b54499d1a2.png)


2. Car module


      ![car](https://user-images.githubusercontent.com/42478821/150472632-15bc197e-83dd-46dc-a6f0-2d37cfa91a61.png)

3. Users


      ![users](https://user-images.githubusercontent.com/42478821/150472686-e90c3800-50e5-4580-8d97-2e1bf7311da6.png)

4. City

      
      ![city](https://user-images.githubusercontent.com/42478821/150472742-7cc9e9f8-b3dd-4341-bcb2-8ace61e11618.png)

5. Tracking


      ![tracking](https://user-images.githubusercontent.com/42478821/150472784-312e06ff-2eb0-4c78-acca-fe4156a65092.png)


### Operator Dashboard ###

1. Login - Please provide try to login with 6 digit code being given at the time of assignment. Once login is successful, Corresponding file must be prompted to download. Please refresh the page manually, modules will be available on the side menu. 


![user-login](https://user-images.githubusercontent.com/42478821/150473401-16d0aea3-5764-45bf-8ab8-fb999de1b642.png)

2. Navigation


![navigation](https://user-images.githubusercontent.com/42478821/150474007-54812fe5-aa84-4ec8-aeec-d39998433ea4.png)


