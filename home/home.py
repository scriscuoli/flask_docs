from flask import Blueprint,render_template,redirect,session
import util
from home.query import get_scanned_file_count
from documents.query import get_document_count
from pages.query import get_page_count,get_documented_page_count
home_bp = Blueprint('home_bp', __name__,
                     template_folder='templates')

@home_bp.route('/')
def show_home():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":util.getSiteName() + " - Home Page",
        "pageTitle": "",
        "pageDescription": ""
    }
    summary = {}
    sfc= get_scanned_file_count()[0]
    pc = get_page_count()
    summary['sfc'] = sfc['scanned_file_count']
    summary['pc'] = get_page_count()
    summary['dpc'] = get_documented_page_count()
    summary['upc'] = summary['pc'] - summary['dpc']
    summary['total_documents'] = get_document_count()
    return render_template('home/home.html',summary=summary,tvals=tvals)
