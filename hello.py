#!/usr/bin/python3
from bottle import route, run, template

@route('/hello')
def hello():
    return "Hello World!"

@route('/world')
def hello():
    return "Hello India World!"
