## CS425 Final Project ##
----------
Web application with database functionalities. Some features are:

 - Movie list
 - Theater list
 - User management
 - Tier rewards
 - Forum


### How to run

This project has been coded using Python with the framework Django. In order to run it, you need the following requirements:
- Python
- Pip
- Django
- Requirements defined in requirements.txt

After installing all the requirements, you need to migrate the databases with the command:

$ python manage.py makemigrations

$ python manage.py migrate

Finally, to run it, you have to execute:

$ python manage.py runserver

However, to make the task easier, the project is up and running in a PaaS called Heroku, that offers free hosting for your apps. The URL is the following:

https://floating-castle-2402.herokuapp.com/