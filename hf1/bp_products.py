from flask import Blueprint, render_template
from hf1.models import artikel_models
from hf1.database import db
from datetime import datetime

bp_products = Blueprint('bp_products', __name__, url_prefix='/products',
                        template_folder='templates')


@bp_products.route('/')
def index():
    artikelgroepen = artikel_models.Artikelgroep.query.all()
    return render_template('products.html',
                           title='Producten',
                           year=datetime.now().year,
                           message='Onze producten',
                           artikelgroepen=artikelgroepen)
