from flask import (Blueprint, render_template, flash, redirect, url_for)
from blueprints.yt2spec.forms import SpecForm
import json
import requests
import os
import shutil
from PIL import Image
from io import BytesIO

yt2spec = Blueprint('yt2spec', __name__, template_folder='templates')


@yt2spec.route('/yt2spec', methods=['GET', 'POST'])
def index():
    form = SpecForm()
    if form.validate_on_submit():
        flash('YouTube URL submitted: %s' %
              form.yt_url.data)

        # Make request to yt2spec API.
        yt2spec_url = 'http://yt2spec:6060/yt2melspec'.rstrip()
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            'url': 'https://www.youtube.com/watch?v=ilNEqmfUyzI',
        }
        response = requests.post(yt2spec_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = json.loads(response.text)
        print(response_json)
        print(response_json['spec_url'])
        spec_url = response_json['spec_url'].rstrip()
        spec_internal_url = 'http://yt2spec:6060' + spec_url
        spec_internal_url = spec_internal_url.rstrip()

        # Use wget/requests to download the spectrogram to the static/images/ directory?
        spec_response = requests.get(spec_internal_url, stream=True)
        if spec_response.status_code == 200:
            i = Image.open(BytesIO(spec_response.content))
            i.save('/usr/local/src/app/qwerty.png')
            os.rename('qwerty.png', './static/images/qwerty2.png')

        return render_template(
            'yt2spec/display_spec.html',
            spec_img_url=url_for('static', filename='images/qwerty2.png')
        )
    return render_template('yt2spec/index.html', title='Placeholder', form=form)
