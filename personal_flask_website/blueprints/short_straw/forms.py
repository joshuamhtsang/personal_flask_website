from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ListForm(FlaskForm):
    choices_list_str = StringField('Choices List',
                         validators=[
                             DataRequired(),
                             Length(min=1, max=1000,
                                    message='Min 1 character, max 1000 chracters.')]
                         )
    submit = SubmitField('Submit')
