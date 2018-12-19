FHIR MongoDB Python Lab
========================

Experimenting with
- FHIR
- MongoDB
- Python and Flask

## Pre-requisites

1. Docker and docker-compose installed
2. Python installed
3. [Virtualenv](https://docs.python-guide.org/dev/virtualenvs/)

## Instructions

1. Run mongoDB and mongo-express with docker-compose. GO to `src` and run `docker-compose up`
2. In a new terminal, in the root of this project, create a python virtual environment `virtualenv .`
3. Activate environment `source bin/activate`
4. Install pip requirements `pip install -r requirements.txt`
5. Change directory `cd src`
6. Load data to mongoDB `python load.py`
7. Run Flask web app `FLASK_APP=main.py flask run`
