# Web Framework: Python-Django

## [Set up Virtual Environment]

* Create the django folder and subdirectory in virtual environemnt 
```sh
$ mkdir django 
$ cd django
$ virtualenv myenv
```

* Activate subdirectory myenv where everything is installed. 
```sh
$ source myenv/bin/activate
```
## [Install Necessary Packages]

* Install Django 1.11.5
```sh
$ pip install Django==1.11.5
```

* Install Bokeh: interactive visualization library
```sh
$ pip install bokeh
```

* Install postgresql python package 
```sh
$ pip install psycopg2
```

* Write all installed packages into the requirements.txt
```sh
$ pip freeze > requirements.txt
```

## [Start with Django Project] 

* Create Django project- Pollution 
```sh
$ django-admin startproject pollution
```

## [Configure PostgreSQL Database and Django backend]

* Change database setting from sqlite3 to postgreSQL in "settings.py"
```sh

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {'options': '-c search_path=public'}
        'NAME': 'pollution',
        'USER': 'postgres',
        'PASSWORD': 'Abcd0101'
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

* Create Django application- statistics
```sh
$ django-admin startapp statistics
```

* Register application by updating INSTALLED_APPS tuple in the settings.py file (add application name)
```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'statistics',
]
```

* Initiate the database to access Admin Interface before launching server
```sh
$ python manage.py migrate
```

## [Create Super User]

```sh
$  python manage.py createsuperuser
```

```sh
(myenv) yuanhsins-MacBook-Air:pollution yuanhsinhuang$ python manage.py createsuperuser
Username (leave blank to use 'yuanhsinhuang'): yuanhsinhuang
Email address: yuanhsin8311@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```




## [Execute Django Server]

* Run a command in a new container
```sh
$ python manage.py runserver
```

* Before launching your server, to access your Admin Interface, you need to initiate the database −
```sh
$ python manage.py migrate
```




















