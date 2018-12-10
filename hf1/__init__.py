import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
    render_template
from flask_sqlalchemy import SQLAlchemy

from .models import db,Todo,init_app

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    # SQLALCHEMY_DATABASE_URI='sqlite:///./test.db',
    SQLALCHEMY_TRACK_MODIFICATIONS='false',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + app.instance_path + '/' + __name__ + '.db',
    SECRET_KEY='DEV')

print(app.config['SQLALCHEMY_DATABASE_URI'])
# load the instance config, if it exists
# app.config.from_pyfile('config.py', silent=True)

db.init_app(app)

init_app(app)


@app.route('/')
def show_all():
    return render_template('show_all.html',
                           todos=Todo.query.order_by(
                               Todo.pub_date.desc()).all()
                           )


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['title']:
            flash('Title is required', 'error')
        elif not request.form['text']:
            flash('Text is required', 'error')
        else:
            todo = Todo(request.form['title'], request.form['text'])
            db.session.add(todo)
            db.session.commit()
            flash(u'Todo item was successfully created')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/update', methods=['POST'])
def update_done():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('show_all'))
