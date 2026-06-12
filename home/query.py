import util
import math
from decimal import *
from datetime import datetime

dbname = util.dbname

def get_scanned_file_count():
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = "select count(*) as scanned_file_count from scanned_files;"
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    return myresult

def get_page_count():
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = "select count(*) as total_pages from pages;"
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    return myresult