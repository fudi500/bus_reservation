// Instruction for linux system. (on Windows you need install python at the begining)

You need to be on dictionery 'bus_reservation' where is file 'mange.py'

    $ cd bus_reservation

You need create virtual enviroment

    $ python3 -m venv myvenv

To activate virtualenv

    $ source myvenv/bin/activate

    // deactivate if needed
        $ deactivate

Install django in project when virtualenv is activated

    (myvenv) $ pip install django==1.8

Create database

    (myvenv) $ python manage.py migrate

Create user

    (myvenv) $ python manage.py createsuperuser


Run local server

    (myvenv) $ python manage.py runserver

You can see aplication on site in browser:

    127.0.0.1:8000
