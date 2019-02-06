from flask import (Blueprint, render_template, flash, redirect, url_for)
from personal_flask_website.blueprints.yt2spec.forms import SpecForm

yt2spec = Blueprint('yt2spec', __name__, template_folder='templates')


@yt2spec.route('/yt2spec', methods=['GET', 'POST'])
def index():
    form = SpecForm()
    if form.validate_on_submit():
        flash('YouTube URL submitted: %s' %
              form.yt_url.data)
        return redirect(url_for('blog.index'))
    return render_template('yt2spec/index.html', title='Placeholder', form=form)
