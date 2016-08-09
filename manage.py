#!/usr/bin/env python
# coding=utf-8
import os
from app import create_app, db
from app.models import Score
from app import spider
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.config['SECRET_KEY'] = 'hard to guees string'
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, spider=spider, Score=Score)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()