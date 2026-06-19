import util
import math
from decimal import *
from datetime import date, timedelta

dbname = util.dbname

def create_document(dc_name:str, dc_date:str):
    dc_id = 0
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"insert into documents (dc_name,dc_date) values ('{dc_name}','{dc_date}');"
    #print(sqlString)
    
    cursor.execute(sqlString)
    dc_id = cursor.lastrowid
    connection.commit()
    return dc_id

def get_document_count():
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = "SELECT count(*) as document_count FROM `documents` WHERE 1;"
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    rtn = 0
    for row in full_set:
        rtn = row['document_count']
    return rtn

def get_documents(days_back:int):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = "SELECT * FROM `documents` dc WHERE 1;"
    if days_back > 0:
        days_ago = date.today() - timedelta(days=days_back)
        formatted_date = days_ago.strftime("%Y-%m-%d")
        sqlString = f"SELECT * FROM `documents` dc WHERE dc.dc_date > '{formatted_date}' order by dc.dc_date,dc.dc_name;"
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    return full_set

def get_document(dc_Id):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT * FROM `documents` dc WHERE dc_id = {dc_Id}"
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    return full_set