#!/usr/bin/env python
from bottle import route, request, run, template # $ pip install bottle

name = None
message = None

@route('/')
def index():
    global name
    global message
    name = request.query.name or name
    message = request.query.message or message

    # return template('<b>Temperature: {{temperature}}</b>',
    #                 temperature=temperature)
    return template('<b>Hello {{name}}! {{message}}!</b>',
                    name=name,message=message )

run(host='localhost', port=8000)