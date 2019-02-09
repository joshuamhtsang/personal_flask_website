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

        # Make request to yt2spec api.
        yt2spec_url = 'http://yt2spec:6060/yt2melspec'
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            'url': 'https://www.youtube.com/watch?v=ilNEqmfUyzI',
        }
        response = requests.post(yt2spec_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = json.loads(response.text)
        print("HELLO!!!!!!")
        print(response_json)
        print(response_json['spec_url'])
        spec_url = response_json['spec_url']
        spec_internal_url = yt2spec_url + spec_url

        return render_template('yt2spec/display_spec.html', yt2spec_internal_url=spec_internal_url)
        #return redirect(yt2spec_url + response_json['spec_url'])
        #return redirect(url_for('blog.index'))
    return render_template('yt2spec/index.html', title='Placeholder', form=form)
