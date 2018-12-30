#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-20 下午4:54
# @Author  : Moon
# @File    : models.py
# @Software: PyCharm


from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Question(db.Model):
    __tablename__='question'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text, nullable=False)
    #now()firsttime
    #now current time
    creat_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref = db.backref('question'))



class Answer(db.Model):
    __tablename__='answer'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    creat_time = db.Column(db.DateTime,default=datetime.now)
    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    question = db.relationship('Question',backref=db.backref("answers",order_by=id.desc()))

    author = db.relationship('User',backref = db.backref('answers'))