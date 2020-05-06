#!/usr/bin/env venv/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'hello world\n'

@app.route('/hello/<username>')
def hello_user(username):
    return ("halli hallo, %s\n" % username)

if __name__=="__main__":
    app.run(host='0.0.0.0')