from flask import Blueprint,render_template,redirect,session,url_for
import util
from documents.query import get_documents,get_document
from pages.query import get_pages_for_doc

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
    result = get_documents(60)
    return render_template('documents/documents.html',result=result,tvals=tvals)

@documents_bp.route('/details/<int:dc_id>')
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
    print("----------------")
    doc_details = get_document(dc_id)
    print(doc_details)
    print("----------------")
    pages = get_pages_for_doc(dc_id)
    print(pages)
    print("----------------")
    updated = add_to_pages(pages)
    print(updated)
    return render_template('documents/document_details.html',doc_details=doc_details[0],pages=updated,tvals=tvals)

def add_to_pages(pages:list):
    rtn = []
    pg_root = url_for('static', filename='images/pages')
    for r in pages:
        row = r.copy()
        ymd = util.get_pdf_file_date(row["pg_path"])
        row['pg_url'] = f"{pg_root}/{ymd['year']}/{ymd['month']}/{row['pg_path']}"
        rtn.append(row)
    return rtn