from flask import Blueprint,render_template,redirect,session
import util

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