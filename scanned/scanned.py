from flask import Blueprint,render_template,redirect,session,request,current_app,url_for
from util import getSiteName,dbname,get_pdf_file_date
from config import Config
from scanned.query import get_scanned
from scanned.forms import DaysBackForm
from pages.query import get_undocumented_page_ids_for_scan_file
import os


scanned_bp = Blueprint('scanned_bp', __name__,
                     template_folder='templates',
                     static_url_path='scanned')

@scanned_bp.route('/',methods=['GET','POST'])
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
    form = DaysBackForm()
    daysBack = 120
    if form.validate_on_submit():
        daysBack = int(form.days_back.data)
    else:
        form.days_back.data = str(daysBack)
    result = get_scanned(daysBack)
    updated_result = add_to_result(result)
    #print(updated_result)
    
    return render_template('scanned/scanned.html',form=form,result=updated_result,tvals=tvals)


def add_to_result(result:list):
    rtn = []
    sf_root = url_for('static', filename='images/pdfs')
    pg_root = url_for('static', filename='images/pages')
    for r in result:
        row = r.copy()
        upa = get_undocumented_page_ids_for_scan_file(r['sf_id'])
        ups = ""
        lupa = len(upa)
        if lupa > 0:
            ex="pages"
            if lupa == 1:
                ex="page"
            ups = f"Undoc: {lupa} {ex}"
        row['ups'] = ups
        ymd = get_pdf_file_date(row["sf_path"])
        row['sf_url'] = f"{sf_root}/{ymd['year']}/{ymd['month']}/{row['sf_path']}"
        row['pg_url'] = f"{pg_root}/{ymd['year']}/{ymd['month']}/{row['pg_path']}"
        rtn.append(row)
    return rtn