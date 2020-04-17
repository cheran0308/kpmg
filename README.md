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

## Tech Stack
This web application uses:

* Ubuntu 18.04 LTS (OS)
* Python 3.6
* Django
* Mysql as a Database (mysqlclient)
