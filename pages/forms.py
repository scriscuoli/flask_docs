from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, TextAreaField,HiddenField
from wtforms.validators import DataRequired,Length

class CreateDocumentForm(FlaskForm):
    command = StringField("Command", validators=[DataRequired(), Length(min=1,max=50)])
    submit = SubmitField('Create Documents')