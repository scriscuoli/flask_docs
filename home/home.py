from flask import Blueprint,render_template,redirect,session
import util
from home.query import get_scanned_file_count,get_page_count

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
    pc = get_page_count()[0]
    summary['sfc'] = sfc['scanned_file_count']
    summary['pc'] = pc['total_pages']
    return render_template('home/home.html',summary=summary,tvals=tvals)
