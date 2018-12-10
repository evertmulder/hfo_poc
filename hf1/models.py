# from sqlalchemy import Column, Integer, String
# from flask_sqlalchemy import SQLAlchemy
# import click
# from flask import current_app, g
# from flask.cli import with_appcontext
# from datetime import datetime
# db = SQLAlchemy()

# class Todo(db.Model):
#     __tablename__ = 'todos'
#     id = db.Column('todo_id', db.Integer, primary_key=True)
#     title = db.Column(db.String(60))
#     text = db.Column(db.String)
#     done = db.Column(db.Boolean)
#     pub_date = db.Column(db.DateTime)

#     def __init__(self, title, text):
#         self.title = title
#         self.text = text
#         self.done = False
#         self.pub_date = datetime.utcnow()

# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(db.Integer, primary_key=True)
#     name = Column(db.String(50), unique=True)
#     email = Column(db.String(120), unique=True)

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % (self.name)

# def init_db():
#     db.create_all()

# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')

# def init_app(app):
#     # app.teardown_appcontext(close_db)
#     # print('init_db_command')
#     app.cli.add_command(init_db_command)