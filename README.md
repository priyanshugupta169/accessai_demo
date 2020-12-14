# Accessai Demo

# Steps to Build and Deploy Django Web App

1 - Install Python 3.7 from https://www.python.org/downloads
2 - Create virtual environment by executing following commands :
        - pip install virtualenvwrapper
        - mkvirtualenv {env_name}
3 - Install Django in virtual environment :
        - pip install django
4 - Go to the project folder and execute the commands to Create Database and Tables :
        - python manage.py makemigration
        - python manage.py migrate
5 - Collect all static files :
        - python manage.py collectstatic
6 - Start the django server :
        - python manage.py runserver
7 - Now you are ready to go with url 127.0.0.1:8000 on browser