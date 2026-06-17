from flask import Blueprint,render_template,redirect,session,request,current_app,url_for
from util import getSiteName,dbname,get_pdf_file_date,parseDocumentCommand
from config import Config
from pages.query import get_pages_for_scanned_file,get_undocumented_pages_for_scanned_file,create_document_from_spec
from pages.forms import CreateDocumentForm
import os


pages_bp = Blueprint('pages_bp', __name__,
                     template_folder='templates',
                     static_url_path='pages')

@pages_bp.route('/<int:sf_id>',methods=['GET','POST'])
def show_pages(sf_id:int):
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": getSiteName(),
        "database" : dbname,
        "name": session.get("name"),
        "title":"Pages",
        "pageTitle": "",
        "pageDescription": ""
    }
    form = CreateDocumentForm()
    if form.validate_on_submit():
        command = form.command.data
        specs = parseDocumentCommand(command)
        for spec in specs:
            create_document_from_spec(sf_id,spec)
        #print(f"specs={specs}")
        form.command.data = ""
    result = get_pages_for_scanned_file(sf_id,False)
    updated_result = add_to_result(sf_id,result)
    #print(updated_result)
    
    return render_template('pages/pages.html',form=form,result=updated_result,tvals=tvals)


def add_to_result(sf_id:int,result:list):
    rtn = []
    upl = get_undocumented_pages_for_scanned_file(sf_id)
    pg_root = url_for('static', filename='images/pages')
    for r in result:
        row = r.copy()
        ymd = get_pdf_file_date(row["pg_path"])
        row['pg_url'] = f"{pg_root}/{ymd['year']}/{ymd['month']}/{row['pg_path']}"
        if row['pg_id'] in upl:
            row['undoc'] = 1
        else:
            row['undoc'] = 0
        rtn.append(row)
    return rtn