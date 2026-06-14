from flask import Blueprint,render_template,redirect,session,request,current_app
from util import getSiteName,dbname,pdf_image_pull
from config import Config
from upload.query import add_pdf_to_db,add_thumbnails_to_db,update_sf_page_count
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
        cfg = current_app.config['CFG']
        pdfs_subfolder = cfg.get_file_location(f.filename,folder_only=True)
        os.makedirs(pdfs_subfolder,exist_ok=True)
        full_pdf_filename = cfg.get_file_location(f.filename)
        f.save(full_pdf_filename)
        sf_id = add_pdf_to_db(f.filename)
        ym = cfg.get_year_month(f.filename)
        thumbnails_dir = f"{cfg.THUMBNAILS_FOLDER}{os.sep}{ym}"
        os.makedirs(thumbnails_dir,exist_ok=True)
        thumbnails = pdf_image_pull(full_pdf_filename,thumbnails_dir)
        update_sf_page_count(sf_id,len(thumbnails))
        th = add_thumbnails_to_db(sf_id=sf_id,thumbnails=thumbnails)
        #print(thumbnails)
    return render_template('upload/upload_handler.html',tvals=tvals)