# python-docker
Python Docker Example

Create a python docker example for the assignment 3.04

The following are the instructions done to deploy this docker for python:

1. Create a repository in github called "python-docker"
2. Run the code below:

$ cd /path/to/python-docker
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install Flask
$ python3 -m pip freeze > requirements.txt
$ touch app.py

3. Add below code to "app.py" file in python-docker folder:

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This is using Python to create a docker image for assignment 3.04'

4. Test the application with the following instructions:

$ cd /path/to/python-docker
$ source .venv/bin/activate
$ python3 -m flask run

5. Create a "Dockerfile" file and add the code below:

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

6. Build Docker image using the command:
$ docker build --tag python-docker .

7. Run Docker image inside container using the command:
$ docker run python-docker

8. Map the host's port 80 to container's port 5000:
$ docker run --publish 8000:5000 python-docker

Reference:
https://docs.docker.com/language/python/build-images/
https://docs.docker.com/language/python/run-containers/
