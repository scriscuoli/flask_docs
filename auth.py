import util
import mysql.connector

dbname = "finance"

def checkUserPass(user,pwd):
    rtn = False

    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
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
        rtn = rtn | v

    return rtn

