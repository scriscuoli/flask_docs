from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired,Length

class DaysBackForm(FlaskForm):
    dc_days_back = StringField("Days Back", validators=[DataRequired()])
    submit = SubmitField('Show')

class UpdateDocumentForm(FlaskForm):
    dc_name = StringField("Name", validators=[DataRequired(), Length(min=1,max=20)])
    dc_date = DateField("Document Date",format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Update Document')