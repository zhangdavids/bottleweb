#! /usr/bin/env python2.7
# coding=utf-8

from bottle import route, run
from bottle import template, static_file

assets_path = './assets'

# @route('/assets/<filename:re:.*\.png>')
# def server_static(filename):
#

@route('/assets/<filename:re:.*\.css|.*\.js|.*\.png|.*\.jpg|.*\.gif>')
def server_static(filename):
    """定义/assets/下的静态(css,js,图片)资源路径"""
    return static_file(filename, root=assets_path)


@route('/assets/<filename:re:.*\.ttf|.*\.otf|.*\.eot|.*\.woff|.*\.svg|.*\.map>')
def server_static(filename):
    """定义/assets/字体资源路径"""
    return static_file(filename, root=assets_path)


@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return template('login')     #login是模板名，这里不需要填写后缀.tpl

@route('/info')
def info():
    name = 'tony'
    age = '18'
    qq = '12456809'
    blog = 'www.github.com'
    return template('info', tname=name, tage=age, tblog=blog,tqq=qq)

run(host='0.0.0.0', port=8999, debug=True)
