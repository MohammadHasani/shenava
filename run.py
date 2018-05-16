from flask import Flask
from src import app
from src.app import *

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0')


