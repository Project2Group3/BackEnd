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
### python -m pip install django

For macOS
### python3 -m venv .venv
### source .venv/bin/activate
Virtual Enviroment is now running, install Django
### python3 -m pip install django
pip install djangorestframework

## Run Locally
In Terminal run
### cd .\publish\
### python manage.py runserver

To view, open Webpage at http://127.0.0.1:8000/
To close, click Ctrl+C or Command+C

To close Virtual Environment, type deactivate and click Return/Enter
