from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SpecForm(FlaskForm):
    yt_url = StringField('YouTube URL', validators=[DataRequired()])
    submit = SubmitField('Submit')
