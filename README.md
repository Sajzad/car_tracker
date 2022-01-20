# Car-Tracker
This README would normally document whatever steps are necessary to get your application up and running.

### Tech. used in the porject? ###

* DRF
* python >=3.6
* Django
* Vue Js

### How do I get set up? ###

* Clone the repo: ```git clone https://github.com/Sajzad/car_tracker.git```.

* Install virtualenv on your system. For linux: ```pip install virtualenv```.

* Go to car_tracker dir. And create virtual environment with virtualenv: ```virtualenv -p /usr/bin/python3 .env```.

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
