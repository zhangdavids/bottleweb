#! /usr/bin/env python2.7
# coding=utf-8

from bottle import route,run

@route('/hello/<name>')
def hell0Name(name):
    return "Hello: %s!" %name

run(host='0.0.0.0', port=8999)
