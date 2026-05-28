import util
import mysql.connector
import subprocess

dbname = util.dbname



        


def getUser(uid):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor(dictionary=True)
    sqlString = f"select * from {table} where  {icol} = {uid}"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    myresult = cursor.fetchone()
    result = {
        "id" : myresult[icol],
        "user": myresult[ucol],
        "pass": myresult[pcol]
    }
    return result

def getUserList():
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    icol=config["idColumn"]
    cursor = connection.cursor(dictionary=True)
  
    sqlString = f"select * from {table} order by {ucol}"

    print(dbname + ": " + sqlString)
    
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    nres = []
    for row in myresult:
        newRow = {
            "id": row[icol],
            "user" : row[ucol],
            "pass" : row[pcol],
        }
        nres.append(newRow)
    return nres

def updateName(uid,newName):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor(dictionary=True)
    sqlString = f"update {table} set {ucol} = '{newName}' where  {icol} = {uid}"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    connection.commit()

def updatePassword(uid,newPassword):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor(dictionary=True)
    sqlString = f"update {table} set {pcol} = '{newPassword}' where  {icol} = {uid}"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    connection.commit()

def deleteUser(uid):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor(dictionary=True)
    sqlString = f"delete  from {table} where  {icol} = {uid}"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    connection.commit()

def addUser(name,pwd):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]

    cursor = connection.cursor(dictionary=True)
    sqlString = f"insert into {table} ({ucol}, {pcol}) values ('{name}','{pwd}')"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    connection.commit()