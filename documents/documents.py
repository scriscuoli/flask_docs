from flask import Blueprint,render_template,redirect,session
import util

documents_bp = Blueprint('documents_bp', __name__,
                     template_folder='templates',
                     static_url_path='documents')

@documents_bp.route('/')
def show_documents():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Documents",
        "pageTitle": "",
        "pageDescription": ""
    }
    return render_template('documents/documents.html',tvals=tvals)