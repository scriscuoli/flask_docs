from flask import Blueprint,render_template,redirect,session,request
import util
import os


upload_bp = Blueprint('upload_bp', __name__,
                     template_folder='templates',
                     static_url_path='upload')

@upload_bp.route('/')
def show_upload():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
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
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Upload Handler",
        "pageTitle": "",
        "pageDescription": ""
    }
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join('test-data/drop', f.filename))
    return render_template('upload/upload_handler.html',tvals=tvals)