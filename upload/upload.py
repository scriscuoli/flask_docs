from flask import Blueprint,render_template,redirect,session,request,current_app
from util import get_year_month,getSiteName,dbname
from config import Config

import os


upload_bp = Blueprint('upload_bp', __name__,
                     template_folder='templates',
                     static_url_path='upload')

@upload_bp.route('/')
def show_upload():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": getSiteName(),
        "database" : dbname,
        "name": session.get("name"),
        "title":"Upload",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('upload/upload.html',tvals=tvals)

@upload_bp.route('/handler', methods=['POST'])
def show_upload_handler():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": getSiteName(),
        "database" : dbname,
        "name": session.get("name"),
        "title":"Upload Handler",
        "pageTitle": "",
        "pageDescription": ""
    }
    if request.method == 'POST':
        pdfs_folder = current_app.config.get("PDFS_FOLDER")
        f = request.files.get('file')
        subdir = get_year_month(f.filename)
        pdfs_subfolder = f"{pdfs_folder}/{subdir}"
        os.makedirs(pdfs_subfolder,exist_ok=True)
        f.save(os.path.join(pdfs_subfolder, f.filename))
    return render_template('upload/upload_handler.html',tvals=tvals)