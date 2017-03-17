# Bus reservation
The project designed to develop the skills of programming Python + Django. Specification involved the application that will allow to book bus with driver for excursions.  The project also can be used to manage car rental and booking cars by customers online.


#### Facilities:
* add, edit, delete buses 
  * admin panel http://[...]/panel
* reservation bus
  * validation if date is correct, if is available
  * counts price of the service
* a few database models witch forienkeys
* sending email to the customer after reservation
  * You need to configure before the first use
* sening SMS do the driver after reservation 
  * Used SMSapi https://www.smsapi.pl/
* design mede using Bootstrap 
  
#### In the project I used:
* Python
* Django
* Git
* Bootstrap
* Linux
  
### You can see the ten project online here:
  - http://fudi555.pythonanywhere.com/
  

### How ro run on linux. 
// On Windows you need install Python before

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
