#! /usr/bin/env python2.7
# coding=utf-8

from bottle import route, run
from bottle import template, static_file, request

assets_path = './assets'
download_path = './download'
save_path = './upload'

# @route('/assets/<filename:re:.*\.png>')
# def server_static(filename):
#

#文件上传的HTML模板，这里没有额外去写html模板了，直接写在这里，方便点吧
@route('/upload')
def upload():
    return '''
        <html>
            <head>
            </head>
            <body>
                <form action"/upload" method="post" enctype="multipart/form-data">
                    <input type="file" name="data" />
                    <input type="submit" value="Upload" />
                </form>
            </body>
        </html>
    '''


@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('data')
    import os.path
    name, ext = os.path.splitext(upload.filename)  # 用os.path.splitext方法把文件名和后缀相分离
    upload.filename = ''.join(('123', ext))  # 修改文件名
    upload.save(save_path, overwrite=True)  # 把文件保存到save_path路径下
    return u'上传成功  原文件名是：%s  文件后缀名是：%s \n 修改后的文件名是：%s' % (name, ext, ''.join(('123', ext)))


#强制文件下载
@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=download_path, download=filename)

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
