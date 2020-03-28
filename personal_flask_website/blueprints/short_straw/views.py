from flask import (Blueprint, render_template, flash)
from blueprints.short_straw.forms import ListForm, RandomDrawForm
import requests
import json

short_straw = Blueprint('short_straw', __name__, template_folder='templates')


@short_straw.route('/shortstraw', methods=['GET', 'POST'])
def index():
    # ListForm()
    list_form = ListForm()
    if list_form.validate_on_submit():
        flash('List submitted: %s' % list_form.choices_list_str.data)

        # Make request to short_straw API.
        url = 'http://shortstraw:2828/sessions'
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "name": "whatever",
            "choices": list_form.choices_list_str.data,
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response.raise_for_status()
        except Exception as e:
            return data

        return "The session id is %s." % response.text

    # RandomDrawForm()
    draw_form = RandomDrawForm()
    if draw_form.validate_on_submit():
        flash('Draw from session: %s' % draw_form.session_id_str)

    return render_template('short_straw/index.html', title='Placeholder',
                           list_form=list_form, draw_form=draw_form)
