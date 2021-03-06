from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/cv')
def cv():
    return render_template('page/cv.html')


@page.route('/aboutme')
def aboutme():
    return render_template('page/aboutme.html')

