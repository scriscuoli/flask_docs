from flask import Blueprint,render_template,redirect,session,url_for
import util
from documents.query import get_documents,get_document,update_document,get_distinct_document_names,find_docs,get_documents_by_date_range
from pages.query import get_pages_for_doc
from documents.forms import DaysBackForm,UpdateDocumentForm,DocumentFindForm
from datetime import date

documents_bp = Blueprint('documents_bp', __name__,
                     template_folder='templates',
                     static_url_path='documents')

@documents_bp.route('/cards',methods=['GET','POST'])
def show_documents_as_cards():
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
    form = DaysBackForm()
    daysBack = 120
    if form.validate_on_submit():
        daysBack = int(form.dc_days_back.data)
    else:
        form.dc_days_back.data = str(daysBack)
    result = get_documents(daysBack)
    colored = add_color(result)
    return render_template('documents/documents_cards.html',form=form,daysBack=daysBack,result=colored,tvals=tvals)

@documents_bp.route('/table',methods=['GET','POST'])
def show_documents_as_table():
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
    form = DaysBackForm()
    daysBack = 120
    if form.validate_on_submit():
        daysBack = int(form.dc_days_back.data)
    else:
        form.dc_days_back.data = str(daysBack)
    result = get_documents(daysBack)
    colored = add_color(result)
    return render_template('documents/documents_table.html',form=form,daysBack=daysBack,result=colored,tvals=tvals)

def add_color(result):
    colors = ["#4b3035","#345a40","#3f456c"]
    curColor = 2
    lastYmd = ""
    rtn = []
    for r in result:
        ymd = str(r['dc_date'])
        if lastYmd != ymd:
            curColor = (1+curColor) % 3
            lastYmd = ymd
        r['color'] = colors[curColor]
        rtn.append(r)
    return rtn

@documents_bp.route('/find/cards',methods=['GET','POST'])
def show_find_cards():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Pages",
        "pageTitle": "",
        "pageDescription": ""
    }
    form = DocumentFindForm()
    dc_name = "Pick"
    today = date.today()
    ds = today
    dc_date_from = ds
    dc_date_to = ds

    if form.validate_on_submit():
        dc_name = form.dc_name_sel.data
        dc_date_from = form.dc_date_from.data
        dc_date_to = form.dc_date_to.data
    else:
        form.dc_name_sel.data = dc_name
        form.dc_date_from.data = dc_date_from
        form.dc_date_to.data = dc_date_to
    result = get_documents_by_date_range(dc_name,dc_date_from,dc_date_to)
    cres = add_color(result)
    return render_template('documents/documents_find_cards.html',form=form,result=cres,tvals=tvals)

@documents_bp.route('/find/table',methods=['GET','POST'])
def show_find_table():
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Pages",
        "pageTitle": "",
        "pageDescription": ""
    }
    form = DocumentFindForm()
    dc_name = "Pick"
    today = date.today()
    ds = today
    dc_date_from = ds
    dc_date_to = ds

    if form.validate_on_submit():
        dc_name = form.dc_name_sel.data
        dc_date_from = form.dc_date_from.data
        dc_date_to = form.dc_date_to.data
    else:
        form.dc_name_sel.data = dc_name
        form.dc_date_from.data = dc_date_from
        form.dc_date_to.data = dc_date_to
    result = get_documents_by_date_range(dc_name,dc_date_from,dc_date_to)
    cres = add_color(result)
    return render_template('documents/documents_find_table.html',form=form,result=cres,tvals=tvals)

@documents_bp.route('/details/<int:dc_id>',methods=['GET','POST'])
def show_document_details(dc_id:int):
    if not session.get("name"):
        return redirect("/DocsApp/login")
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Document Details",
        "pageTitle": "",
        "pageDescription": ""
    }
    form = UpdateDocumentForm()
    doc_details = get_document(dc_id)

    if form.validate_on_submit():
        dc_name = form.dc_name.data
        dc_date = form.dc_date.data
        update_document(dc_id,dc_name,dc_date)
    else:
        form.dc_name.data = doc_details[0]['dc_name']
        form.dc_date.data = doc_details[0]['dc_date']

    
    pages = get_pages_for_doc(dc_id)
    updated = add_to_pages(pages)
    dd = get_distinct_document_names()

    #print(updated)
    return render_template('documents/document_details.html',form=form,dd=dd,pages=updated,tvals=tvals)

def add_to_pages(pages:list):
    rtn = []
    pg_root = url_for('static', filename='images/pages')
    for r in pages:
        row = r.copy()
        ymd = util.get_pdf_file_date(row["pg_path"])
        row['pg_url'] = f"{pg_root}/{ymd['year']}/{ymd['month']}/{row['pg_path']}"     
        rtn.append(row)
    return rtn