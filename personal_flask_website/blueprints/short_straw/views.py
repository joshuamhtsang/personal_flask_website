from flask import (Blueprint, render_template)

short_straw = Blueprint('short_straw', __name__, template_folder='templates')


@short_straw.route('/shortstraw', methods=['GET', 'POST'])
def index():
    return render_template('short_straw/index.html', title='Placeholder')
