from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DaysBackForm(FlaskForm):
    days_back = StringField("Days Back", validators=[DataRequired()])
    submit = SubmitField('Show')