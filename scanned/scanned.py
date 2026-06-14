from flask import Blueprint,render_template,redirect,session,request,current_app,url_for
from util import getSiteName,dbname,get_pdf_file_date
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
    updated_result = add_to_result(result)
    print(updated_result)
    sf_root = url_for('static', filename='images/pdfs')
    pg_root = url_for('static', filename='images/thumbnails')
    return render_template('scanned/scanned.html',result=updated_result,tvals=tvals)


def add_to_result(result:list):
    rtn = []
    sf_root = url_for('static', filename='images/pdfs')
    pg_root = url_for('static', filename='images/thumbnails')
    for r in result:
        row = r.copy()
        ymd = get_pdf_file_date(row["sf_path"])
        row['sf_url'] = f"{sf_root}/{ymd['year']}/{ymd['month']}/{row['sf_path']}"
        row['pg_url'] = f"{pg_root}/{ymd['year']}/{ymd['month']}/{row['pg_path']}"
        rtn.append(row)
    return rtn