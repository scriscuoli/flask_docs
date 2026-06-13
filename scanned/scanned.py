from flask import Blueprint,render_template,redirect,session,request,current_app
from util import getSiteName,dbname,pdf_image_pull
from config import Config
from scanned.query import get_scanned
import os


scanned_bp = Blueprint('scanned_bp', __name__,
                     template_folder='templates',
                     static_url_path='scanned')

@scanned_bp.route('/')
def show_scanned():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": getSiteName(),
        "database" : dbname,
        "name": session.get("name"),
        "title":"Scanned",
        "pageTitle": "",
        "pageDescription": ""
    }
    result = get_scanned()
    print(result)
    return render_template('scanned/scanned.html',tvals=tvals)

