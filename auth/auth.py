from flask import Blueprint,render_template,redirect,session,request
from auth.forms import LoginForm

import util
import mysql.connector

dbname = util.dbname


def checkUserPass(user,pwd):
    rtn = 0

    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    icol=config["idColumn"]
    cursor = connection.cursor(dictionary=True)

    sqlString = f"select * from {table} where {ucol} = '{user}'"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    for row in myresult:
        urv = row[ucol]
        prv = row[pcol]
        #password_verify(password: str, hashed_password: str) -> bool:
        v  = util.password_verify(pwd,prv)
        if v == True:
            rtn = row[icol]

    return rtn

auth_bp = Blueprint('auth_bp', __name__,
                     template_folder='templates')


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    tvals = {
        "site": util.getSiteName(),
        "database" : util.dbname,
        "name": session.get("name"),
        "title":"Login",
        "pageTitle": "",
        "pageDescription": "",
        
    }
    form = LoginForm('auth/login.html')
    if request.method == "POST":
        # Record the user name in session
        n = request.form.get("name")
        p = request.form.get("password")
        id = checkUserPass(n,p)
        if id != 0:
            session["name"] = request.form.get("name")
            session["id"] = id
            return redirect("/DocsApp")
    return render_template("auth/login.html",tvals=tvals,form=form)

@auth_bp.route("/logout")
def logout():
    # Clear the username from session
    session["name"] = None
    session["id"] = None
    return redirect("/DocsApp")
