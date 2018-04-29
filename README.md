# smiles

## Setting up

* Create your virtualenv.

```
# With pew
pew new --python=python3 smiles
# New virtualenv will automatically be activated
```

* Install Django and create the project.

```
pip install django
django-admin startproject --template=https://github.com/sloria/smiles/archive/template.zip smiles
cd smiles
```

* Install requirements

```
pip install -r requirements.txt
```

* Copy the local environment config file.

```
cp .env.example .env
```

* Run the server

```
python manage.py runserver
```

* Browse to http://localhost:8000/ to see your app.

## Deploying to Heroku

```
heroku create
git push heroku master
```

## What this is

A small app used to teach the following concepts:

* Object-oriented programming
* Client-server communication
* What a web framework is/does
* Using 3rd-party Python packages
* Testing

This is used for [Girl Develop It Central Virginia's](https://www.meetup.com/Girl-Develop-It-CentralVA/) Intermediate Python class.

## What this is not

This app is used for teaching very specific concepts and is not
necessarily meant to demonstrate best practices. Furthermore, it
deliberately omits a few things:

* Does NOT teach databases or ORMs
* Does NOT go in-depth into Django's APIs
* Does NOT assume knowledge of HTML/CSS/JS (template files are provided)
* Does NOT teach JSON APIs
* Does NOT teach frontend frameworks


## License

[MIT Licensed](https://sloria.mit-license.org/)
