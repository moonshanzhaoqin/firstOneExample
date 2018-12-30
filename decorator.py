#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-26 下午7:13
# @Author  : Moon.Shan
# @File    : decorator.py
# @Software: PyCharm
from functools import wraps
from flask import redirect,url_for,session

#login
def loin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper