from flask import Blueprint,render_template,redirect,session,request,current_app
from util import getSiteName,dbname
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
        f = request.files.get('file')
        cfg = Config()
        pdfs_subfolder = cfg.get_file_location(f.filename,folder_only=True)
        os.makedirs(pdfs_subfolder,exist_ok=True)
        full_pdf_filename = cfg.get_file_location(f.filename)
        f.save(full_pdf_filename)
    return render_template('upload/upload_handler.html',tvals=tvals)