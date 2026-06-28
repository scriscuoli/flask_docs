from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired,Length

class DaysBackForm(FlaskForm):
    dc_days_back = StringField("Days Back", validators=[DataRequired()])
    submit = SubmitField('Show')