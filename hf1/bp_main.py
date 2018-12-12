from flask import Blueprint, render_template

bp_main = Blueprint('bp_main', __name__,
                    template_folder='templates')


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.route('/contact')
def contact():
    return render_template('contact.html',
                           title='Contact',
                           message='Waar u ons kunt vinden')


@bp_main.route('/about')
def about():
    return render_template('about.html')
