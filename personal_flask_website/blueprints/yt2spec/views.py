from flask import (Blueprint, render_template, flash, redirect, url_for)
from personal_flask_website.blueprints.yt2spec.forms import SpecForm
import json
import requests
import os

yt2spec = Blueprint('yt2spec', __name__, template_folder='templates')


@yt2spec.route('/yt2spec', methods=['GET', 'POST'])
def index():
    form = SpecForm()
    if form.validate_on_submit():
        flash('YouTube URL submitted: %s' %
              form.yt_url.data)

        # Make request to yt2spec rest api call here.
        #os.environ['NO_PROXY'] = '127.0.01'
        #NO_PROXY = {
        #    'no': 'pass'
        #}
        yt2spec_url = 'http://127.0.0.1:6060/yt2melspec'
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            'url': 'https://www.youtube.com/watch?v=ilNEqmfUyzI',
        }
        r = requests.post(yt2spec_url, headers=headers, data=json.dumps(data))
        r.raise_for_status()
        print(r.json())

        return redirect(url_for('blog.index'))
    return render_template('yt2spec/index.html', title='Placeholder', form=form)
