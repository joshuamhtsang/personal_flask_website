from flask import (Blueprint, render_template)
from personal_flask_website.blueprints.yt2spec.forms import SpecForm

yt2spec = Blueprint('yt2spec', __name__, template_folder='templates')


@yt2spec.route('/yt2spec')
def index():
    form = SpecForm()
    return render_template('yt2spec/index.html', title='Placeholder', form=form)
