from flask import (Blueprint, render_template, flash, redirect, url_for)
from blueprints.celery_tester.forms import SleeperForm
import json
import requests
import os
import shutil
import sys
import uuid

celery_tester = Blueprint('celery_tester', __name__, template_folder='templates')


@celery_tester.route('/celerytester', methods=['GET', 'POST'])
def index():
    form = SleeperForm()
    if form.validate_on_submit():
        flash('Sleep duration: %s' % form.sleep_duration.data)

        sleeper_url = 'http://sleeper:1234'.rstrip()
        endpoint_name = 'look_busy'.rstrip()
        sleeper_ep_url = sleeper_url + '/' + endpoint_name
        sleep_duration = form.sleep_duration.data
        payload = {
            'n': sleep_duration
        }
        response = requests.get(sleeper_ep_url, params=payload)
        print(response)
    return render_template('celery_tester/index.html', title='Placeholder', form=form)


