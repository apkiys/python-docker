from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This is using Python to create a docker image for assignment 3.04'
