import click
from flask import current_app, g
from flask.cli import with_appcontext
from hf1.models import account_models, artikel_models
from hf1.database import db

def init_db():
    db.create_all()

def fill_db():
    db.drop_all()
    db.create_all()
    groep_shampoo = artikel_models.Artikelgroep("Shampoo")
    db.session.add(groep_shampoo)
    db.session.add(artikel_models.Artikel(groep_shampoo, "Head & Shoulders", 2.45))
    db.session.add(artikel_models.Artikel(groep_shampoo, "Fanola - No-Yellow Shampoo", 3.25))

    groep_accessoires = artikel_models.Artikelgroep("Nagels")
    db.session.add(artikel_models.Artikel(groep_accessoires, "Acrylnagels", 4.50))
    db.session.add(artikel_models.Artikel(groep_accessoires, "Gelnagels", 3.75))
    db.session.add(artikel_models.Artikel(groep_accessoires, "Nagel tips", 9.95))

    db.session.add(groep_accessoires)

    db.session.add(account_models.Account("Evert", "Mulder", "evertmulder@gmail.com", "06-51500540"))

    db.session.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database %s.' %
               current_app.config['SQLALCHEMY_DATABASE_URI'])

@click.command('fill-db')
@with_appcontext
def fill_db_command():
    """Clear the existing data and create new tables."""
    fill_db()
    click.echo('Cleaning and added test data to database %s.' %
               current_app.config['SQLALCHEMY_DATABASE_URI'])

def init_cli_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)
