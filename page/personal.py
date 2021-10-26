# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:44:37 2021

@author: user
"""
from flask import Flask ,Blueprint,redirect,abort,current_app

person = Blueprint('personal', __name__, template_folder='../templates')#
def errorfunc():
    try:
        x = 5 / 0
        print(x)
    except:
        current_app.logger.error("Catch an exception in personal func.", exc_info=True)
        abort(500)
@person.route('/')
def personal():
    errorfunc()
    #current_app.logger.error("Catch an exception in personal.", exc_info=True)
    #abort(500)
    return 'personal'