from flask import (Blueprint, render_template, flash, redirect, url_for)
from blueprints.yt2spec.forms import SpecForm
import json
import requests
import os
import shutil
from PIL import Image
from io import BytesIO
import sys
import uuid

yt2spec = Blueprint('yt2spec', __name__, template_folder='templates')


@yt2spec.route('/yt2spec', methods=['GET', 'POST'])
def index():
    form = SpecForm()
    if form.validate_on_submit():
        flash('YouTube URL submitted: %s' %
              form.yt_url.data)

        # Get YouTube URL from the form.
        yt_url = str(form.yt_url.data)

        # Make request to yt2spec API.
        yt2spec_url = 'http://yt2spec:6060'.rstrip()
        endpoint_name = 'yt2melspec'.rstrip()
        yt2spec_ep_url = yt2spec_url + '/' + endpoint_name
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            'url': yt_url,
        }
        response = requests.post(yt2spec_ep_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        response_json = json.loads(response.text)
        spec_url = response_json['spec_url'].rstrip()
        spec_internal_url = yt2spec_url + spec_url
        spec_internal_url = spec_internal_url.rstrip()

        # Use requests.get() to download the spectrogram to the static/images/ directory.
        spec_response = requests.get(spec_internal_url, stream=True)
        if spec_response.status_code == 200:
            i = Image.open(BytesIO(spec_response.content))
            spec_filename = str(uuid.uuid4()) + '.png'
            i.save(os.path.join('/usr/local/src/app/', spec_filename))
            os.rename(spec_filename, os.path.join('./static/images/', spec_filename))
            return render_template(
                'yt2spec/display_spec.html',
                spec_img_url=url_for('static', filename='images/' + spec_filename)
            )
        else:
            return render_template(
                'yt2spec/error.html',
                sorry_img_url=url_for('static', filename='images/sorry.png')
            )


    return render_template('yt2spec/index.html', title='Placeholder', form=form)
