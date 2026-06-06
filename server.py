from flask import Flask,render_template, redirect, request,session
from flask_wtf import FlaskForm,CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, FileField
from flask_wtf.file import FileAllowed,FileRequired
from werkzeug.utils import secure_filename
from waitress import serve

import os

from auth.auth import dbname
from about.about import about_bp
from admin.admin import admin_bp
from documents.documents import documents_bp
from home.home import home_bp
from auth.auth import  auth_bp
from upload.upload import upload_bp
from user.user import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDC'
app.config['APP_NAME'] = dbname
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

# blueprints
app.register_blueprint(about_bp,url_prefix='/DocsApp/about')
app.register_blueprint(admin_bp,url_prefix='/DocsApp/admin')
app.register_blueprint(documents_bp,url_prefix='/DocsApp/documents')
app.register_blueprint(home_bp,url_prefix='/DocsApp')
app.register_blueprint(auth_bp,url_prefix='/DocsApp')
app.register_blueprint(upload_bp,url_prefix='/DocsApp/upload')
app.register_blueprint(user_bp,url_prefix="/DocsApp/user")

csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(error):
    return "page_not_found...",404

@app.errorhandler(500)
def you_broke_it(errror):
    return "you_broke_it...",500

mode = "dev"

if __name__ == '__main__':

    if mode == "dev":
        app.run(host='0.0.0.0',port=5000,debug=True)
    else:
        serve(app,host='0.0.0.0',port=5000,threads=2)