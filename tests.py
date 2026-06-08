
import os
import sys
import util
import auth

def test1():
    password="189565174"
    notPassword="8675309"
    hpass = util.password_hash(password)
    #hpass = util.php_password_hash(password)

    ok = util.password_verify(password=notPassword,hashed_password=hpass)

    print("The result is " + str(ok))

def test2():
    password="password"
    hpass="$2y$10$RnnpvftcnRaB60h/.oQq9.JLui062wntcJ6Go251r1DmbW1oySILy"
    ok = util.password_verify(password=password,hashed_password=hpass)

    print("The result is " + str(ok))

def test3():
    password="!QAZ2wsx#EDC4rfv"
    hp1 = [
        "$2y$10$C5jNL3CgJBzWu68dKo0fDOEw19QqpL08dmgxYP7MsEWIUEATsOLJG",
        "$2y$10$dBD8UmnUPRkiL/uETitKIOKo5dVHfD235jgeU2Q/YdfP/rVgTP8By",
        "$2y$10$uLBTQ6puGoxEfGLz5MFGMO.OydVKKoaCJZSrwqn8q9WCdvpUD/Y/6"
        ]
    nhp = util.password_hash(password)
    print("nhp=> " + nhp + "<=")
    for hp in hp1:
        ok = util.password_verify(password,hp)
        
        print("The result is " + str(ok))

def ssnInsert():
    ssna = {
        "steve": "189565174",
        "missie": "215848230",
        "spencer": "215694733"
    }
    connection = util.db_connect(util.accounts_db_config)
    cursor = connection.cursor()
    for k,v in ssna.items():
        print("k=" + k + ",  v=" + v)
        hv = util.password_hash(v)
        print(hv)
        sqlstring = "insert into users (id,pass) values (%s,%s)"
        val = (k,hv)
        
        result = cursor.execute(sqlstring,val)
        connection.commit()
    connection.close()

def adminInsertAccounts():
    ssna = {
        "admin": "password"
    }
    connection = util.db_connect(util.accounts_db_config)
    cursor = connection.cursor()
    for k,v in ssna.items():
        print("k=" + k + ",  v=" + v)
        hv = util.password_hash(v)
        print(hv)
        sqlstring = "insert into users (id,pass) values (%s,%s)"
        val = (k,hv)
        
        result = cursor.execute(sqlstring,val)
        connection.commit()
    connection.close()

def adminInsertCollection():
    ssna = {
        "admin": "password"
    }
    dbname="ncd"
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor()
    for k,v in ssna.items():
        print("k=" + k + ",  v=" + v)
        hv = util.password_hash(v)
        print(hv)
        sqlstring = f"insert into {table} ({ucol},{pcol}) values (%s,%s)"
        val = (k,hv)
        print(sqlstring)
        result = cursor.execute(sqlstring,val)
        connection.commit()
    connection.close()

def showTables(dbname):
    connection = util.db_connect(dbname)
    cursor = connection.cursor()
    sqlstring="show tables;"
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    print("Database: " + dbname)
    for x in result:
        print(x)
    connection.close()

def dbtest1():
    connection = util.db_connect(util.finance_db_config)
    cursor = connection.cursor()
    sqlstring="select * from company"
    sqlstring="describe company"
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    for x in result:
        print(x)
    connection.close()


def dbtest2():
    connection = util.db_connect(util.accounts_db_config)
    cursor = connection.cursor()
    sqlstring="select * from categories"
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    for x in result:
        print(x)
    connection.close()


def dbtest3():
    ssna = {
        "steve": "189565174",
        "missie": "215848230",
        "spencer": "215694733"
    }
    connection = util.db_connect(util.accounts_db_config)
    cursor = connection.cursor(dictionary=True)
    sqlstring="select * from users"
    cursor.execute(sqlstring)
    result = cursor.fetchall()
    connection.close()
    for x in result:
        hpass = x["pass"]
        for id,pw in ssna.items():
            if util.password_verify(pw,hpass) == True:
                print ("Hello " + x["id"])
    
def gymtest():
    print(util.get_year_month("05302026211558.pdf"))  # → 2026/05

def authTest():
    v = auth.checkUserPass("admin","password")
    print("authTest: " + str(v))

if __name__ == "__main__":
    #adminInsertCollection()
    #showTables("collection")
    #showTables("finance")
    #showTables("ncd")
    #test2()
    #adminInsertCollection()
    #authTest()
    gymtest()