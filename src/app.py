# -*- coding: utf-8 -*-
from flask import Flask, render_template
from database import init_db
import models

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    init_db(app)
    return app

app = create_app()


@app.route("/")
def index():
    name = "Hoge"
    return render_template('index.html', title='indexページ', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id
