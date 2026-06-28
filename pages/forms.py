from flask_wtf import FlaskForm
from wtforms import DateField, StringField, PasswordField, SubmitField, TextAreaField,HiddenField
from wtforms.validators import DataRequired,Length

class CreateDocumentForm(FlaskForm):
    dc_name = StringField("Name", validators=[DataRequired(), Length(min=1,max=20)])
    dc_date = DateField("Document Date",format='%Y-%m-%d', validators=[DataRequired()])
    dc_page_spec = StringField("Page Spec", validators=[DataRequired(), Length(min=1,max=20)])
    submit = SubmitField('Create Document')