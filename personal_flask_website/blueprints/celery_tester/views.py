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
    return render_template('celery_tester/index.html', title='Placeholder', form=form)


