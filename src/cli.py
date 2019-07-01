# -*- coding: utf-8 -*-
from flask import Flask
from tasks import task
from database import init_db
import models

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    init_db(app)
    return app

app = create_app()
app.cli.add_command(task)
