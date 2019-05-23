# Limelight API

Powered by Django and SQLite

### Requirements
- Git
- Python

### Installing
Clone this repo
```
git clone https://github.com/limelight-dance/core.git

cd core
```
Set up virtual env and install dependencies
```
pip install pipenv

pipenv shell

pipenv install
```
Run migrations
```
python manage.py migrate
```
### Running
```
python manage.py runserver
```
### Deploying
```sh
# You only need to run the folling line once
heroku git:remote -a limelight-dance-core

git push heroku master
```
