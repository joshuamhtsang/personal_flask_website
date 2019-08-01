from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SleeperForm(FlaskForm):
    sleep_duration = StringField('Sleep duration',
                         validators=[
                             DataRequired(),
                             Length(min=1, max=10,
                                    message='You must enter a valid duration length.')]
                         )
    submit = SubmitField('Submit')
