# How to run Django Project

## Make Branch
in terminal go to directory and call
### git checkout -b branch_name

## Make Virtual Environment 

For Windows
In terminal run
### python -m venv .venv
### Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
### .venv\Scripts\Activate.ps1
Virtual Enviroment is now running, install Django  
### python -m pip install "django>=4.2,<5.0"
### python -m pip install djangorestframework
### pip install mysqlclient
### pip install django-cors-headers




For macOS
### python3 -m venv .venv
### source .venv/bin/activate
Virtual Enviroment is now running, install Django

### pip install "django>=4.2,<5.0"

## To set Connection to database
### brew install openssl
### export LDFLAGS="-L/opt/homebrew/opt/openssl/lib"
### export CPPFLAGS="-I/opt/homebrew/opt/openssl/include"
### pip install mysqlclient
### python manage.py migrate

## Run Locally
In Terminal 
### cd .\publish\
### python manage.py migrate
### python manage.py runserver

To view, open Webpage at http://127.0.0.1:8000/
To close, click Ctrl+C or Command+C

To close Virtual Environment, type deactivate and click Return/Enter
