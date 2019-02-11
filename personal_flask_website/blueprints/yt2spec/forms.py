from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SpecForm(FlaskForm):
    yt_url = StringField('YouTube URL',
                         validators=[
                             DataRequired(),
                             Length(min=12, max=100,
                                    message='YouTube Link must be between 12 and 100 characters long')]
                         )
    submit = SubmitField('Submit')
