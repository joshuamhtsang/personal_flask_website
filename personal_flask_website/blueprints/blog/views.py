from flask import (Blueprint, render_template)

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/blog')
def index():
    return render_template('blog/index.html')

