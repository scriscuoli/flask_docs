from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,Length
from documents.query import get_distinct_document_names
from util import list_to_choices
from datetime import date

class DaysBackForm(FlaskForm):
    dc_days_back = StringField("Days Back", validators=[DataRequired()])
    submit = SubmitField('Show')

class UpdateDocumentForm(FlaskForm):
    dc_name = StringField("Name", validators=[DataRequired(), Length(min=1,max=20)])
    dc_date = DateField("Document Date",format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Update Document')

class DocumentFindForm(FlaskForm):
    #dc_name = StringField("Document Name", validators=[DataRequired()])
    dd = get_distinct_document_names()
    choices = list_to_choices(dd)
    choices.insert(0,("Any","Any"))
    choices.insert(0,("Pick","Pick"))
    dc_name_sel = SelectField("Document Name",choices=choices)
    dc_date_from = DateField("From:",format='%Y-%m-%d', default=date.today, validators=[DataRequired()])
    dc_date_to = DateField("To:",format='%Y-%m-%d', default=date.today, validators=[DataRequired()])
    submit = SubmitField('Find')