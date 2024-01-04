#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5555)
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'