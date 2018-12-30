#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-20 下午5:38
# @Author  : Moon.Shan
# @File    : manage.py
# @Software: PyCharm

from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from app import app
from exts import db
from models import User


manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

if __name__=="__main__":
    manager.run()