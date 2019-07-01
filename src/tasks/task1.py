# -*- coding: utf-8 -*-
import click
from flask.cli import with_appcontext
from models import User

@click.command('task1', help="Hello World.")
@with_appcontext
def task1_run():
    print("hello world!!!!!")
    users = User.get_all()

    if not users:
        print("Not found user...")
    else:
        print("found user...")
