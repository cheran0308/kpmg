# Workflow Management System

## Getting Started
Setting up a Dev Environment
This webapp is a Python 3.6 application.

1. On GitHub, fork the repo by clicking the Fork button in the GitHub UI.
2. Open your terminal, run command **mkdir kpmg**
3. **cd kpmg**
4. Install Virtualenv in your local by running the command **pip install virtualenv**
5. Run the command **virtualenv env**, this will set up the virtual environment with python 3.6, pip and other essential tools.
6. Activate env with **. env/bin/activate**
7. Clone the repo on your local machine with **git clone git@github.com:cheran0308/kpmg.git** and **cd kpmg**
8. Now install the dependencies like django and mysqlclient with **pip install -r requirements.txt**
9. Open **portal/settings.py** and change the database settings according to yours.
10. Run **python manage.py migrate** and then **python manage.py runserver** to run the web application.
11. Go to localhost:8000 in your browser.

## System Design
![system Design](https://github.com/cheran0308/kpmg/blob/master/screenshots/system_design.jpg)

## Tech Stack
This web application uses:

* Python 3.6
* Django
* Mysql as a Database (mysqlclient)
* Redis

## To Create a login user

* Open Terminal and navigate to your project root
* Run **python manage.py shell**
* Run **from app.models import User**
* Run **user=User(name="test", email="test@test.com", password="123456", phone="987654321", dob="01-01-1990")**
* Run **user.save()**

## Installing Redis Cache

* Run Command **wget http://download.redis.io/redis-stable.tar.gz**
* Run **tar xvzf redis-stable.tar.gz**
* Run **cd redis-stable**
* Run **make**
* Run **make test**
* Run **sudo make install**

## Setting up Load Balancer (NGINX)
The Below method shows setting up NGINX in Ubuntu 10.04 LTS

* Run Command **sudo apt-get update**
* Run **sudo apt-get install nginx**
* Verify the Installation by going to http://localhost
* Open /etc/nginx/sites-available/default using **sudo nano /etc/nginx/sites-available/default**
* Adding the below code in it

```
upstream www {
  server localhost:8000;
  server localhost:9000;
  server localhost:8001;
}
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  
  location / {
    proxy_pass http://www;
  }
}
```
* save it, `ctrl+x` and type `y` and **enter**
* Restart the server using **sudo service nginx restart**
* Run the django servers in ports 8000, 9000 and 9001 
* Verify by going to http:localhost
