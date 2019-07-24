#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yxf'

from flask import Flask, escape, url_for, render_template, request, session, send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = '{h║R[HKf,F'
app.config['UPLOAD_FOLDER'] = 'C:/Users/Administrator/Desktop/uploads/'
@app.route('/login',methods={'post','get'})
def login():
    """login api,when method is get,redirect login.html
    post,really login
    other method, illegal
    :return:
    """
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            session['username'] = request.form['username']
            return 'success'
        else:
            error = 'USERNAME OR PASSWORD IS NOT RIGHT'
    elif request.method == 'GET':
        return render_template('login.html')
    else:
        error = 'method not support!'
    return error

@app.route('/upload',methods=['POST'])
def upload():
    """upload api,need login first

    :return:
    """
    if request.method == 'POST' and 'username' in session:
        f = request.files['image']
        f.save('C:/Users/Administrator/Desktop/uploads/'+ secure_filename(f.filename))
        return "success"
    return "error,may be you need login first?"

@app.route('/logout',methods=["GET"])
def logout():
    """logout api

    :return:
    """
    session.pop('username',None)
    return render_template("login.html")

@app.route('/home/',methods=['GET'])
def home():
    if request.method == "GET" and 'username' in session:
        return render_template("user.html")
    else:
        return render_template('login.html')

@app.route('/image/<path:image>')
def image(image):
    """api for visit image.
    :param image:
    :return:
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'],image,as_attachment=False)

def valid_login(username,password):
    """api to judge login info is legal or not

    :param username:
    :param password:
    :return:
    """
    if username=='yxf' and password == 'andfxy':
        return True
    else:
        return False

def login_success():
    pass



