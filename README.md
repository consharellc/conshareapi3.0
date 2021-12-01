#
<div align="center">
<!-- <img src="./static/images/dark-logo.1c6c40e2.png" width="20%"> -->
<b>
<span>
API
</span>
</b>
<h1>Conshare Api Repo</h1>


## Install and Run
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations and create your superuser (follow the prompts)

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

Run the tests

```bash
# run django tests for feed app
python manage.py test feed
```

```bash
# run django tests for users app
python manage.py test users
```

Run the development server

```bash
# run django development server
python manage.py runserver
```
