from flask import Blueprint, render_template, request
from hf1.models import account_models
from hf1.database import db

bp_account = Blueprint('bp_account', __name__, url_prefix='/account',
                       template_folder='templates')


@bp_account.route('/aanmaken')
def maak_account():
    return render_template('maak_een_account_aan.html',
                           title='Registreren',
                           voornaam='',
                           achternaam='',
                           email='',
                           telefoon='')


@bp_account.route('/aanmaken', methods=["POST"])
def post_maak_account():
    voornaam = request.form['voornaam']
    achternaam = request.form['achternaam']
    email = request.form['email']
    telefoon = request.form['telefoon']
    password = request.form['password']

    errors = []
    if len(password) < 5:
        errors.append("Wachtwoord is te kort")
    if len(email) < 1:
        errors.append("E-mailadres is verpicht")
    if voornaam.lower() == 'rudi':
        errors.append("Deze persoon komt er niet in!")

    exising_account = account_models.Account.query.filter_by(
        email=email).first()
    if exising_account:
        errors.append("E-mailadres '%s' is al in gebruik." % email)

    if len(errors) == 0:
        try:
            db.session.add(account_models.Account(
                voornaam, achternaam, email, telefoon))
            db.session.commit()
        except:
            errors.append("Opslaan is niet gelukt!")

    if len(errors) == 0:
        return render_template('bedankt.html')

    return render_template('maak_een_account_aan.html',
                           title='Registreren',
                           voornaam=voornaam,
                           achternaam=achternaam,
                           email=email,
                           telefoon=telefoon,
                           errors=errors)
