# smiles

## What this is

A small app used to teach the following concepts:

* Object-oriented programming
* Client-server communication
* Using 3rd-party Python packages
* What a web framework is/does
* Testing

This was used for the Girl Develop It (Central VA) Intermediate Python class.

## What this is not

* Does NOT teach databases or ORMs
* Does NOT go in-depth into Django's APIs
* Does NOT assume knowledge of HTML/CSS/JS (template file is provided)

## Running locally

* Clone or download this repo.
* Create your virtualenv

```
# With pew
pew new --python=python3 smiles
# New virtualenv will automatically be activated
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

## License

[MIT Licensed](https://sloria.mit-license.org/)
