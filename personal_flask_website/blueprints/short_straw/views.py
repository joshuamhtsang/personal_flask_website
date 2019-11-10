from flask import (Blueprint, render_template, flash)
from blueprints.short_straw.forms import ListForm

short_straw = Blueprint('short_straw', __name__, template_folder='templates')


@short_straw.route('/shortstraw', methods=['GET', 'POST'])
def index():
    form = ListForm()
    if form.validate_on_submit():
        flash('List submitted: %s' % form.choices_list_str)
    return render_template('short_straw/index.html', title='Placeholder', form=form)
