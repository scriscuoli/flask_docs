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

def update_document(dc_id,dc_name,dc_date):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"update documents set dc_name = '{dc_name}', dc_date ='{dc_date}' where dc_id = {dc_id};"
    print(f"upate_document:  ==>{sqlString}<==")
    cursor.execute(sqlString)
    connection.commit()

def get_distinct_document_names():
    rtn = []
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = "SELECT distinct dc_name FROM `documents` dc order by dc_name;"
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    for row in full_set:
        rtn.append(row['dc_name'])
    return rtn

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

def get_documents_by_date_range(dc_name:str, date_from:str, date_to: str):
    result = []
    if dc_name != "Pick":
        connection = util.db_connect(dbname)
        cursor = connection.cursor(dictionary=True)
        sqlString = "SELECT * FROM `documents` dc where "
        if dc_name != "Any":
            sqlString = sqlString + f" dc.dc_name = '{dc_name}' and"
        
        sqlString = sqlString + f" dc.dc_date >= '{date_from}'"
        sqlString = sqlString + f" and dc.dc_date <= '{date_to}'"
        sqlString = sqlString + " order by dc.dc_date,dc.dc_name;"

        print(sqlString)
        cursor.execute(sqlString)
        result = cursor.fetchall()

    return result

def get_document(dc_Id):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT * FROM `documents` dc WHERE dc_id = {dc_Id}"
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    return full_set

def find_docs(dc_name:str, days_back:int):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT dc.* FROM `documents` dc WHERE dc.dc_name = '{dc_name}';"
    if days_back > 0:
        days_ago = date.today() - timedelta(days=days_back)
        formatted_date = days_ago.strftime("%Y-%m-%d")
        sqlString = f"SELECT dc.* FROM `documents` dc WHERE dc.dc_name = '{dc_name}' and dc.dc_date > '{formatted_date}' order by dc.dc_date;"
    
    print(f"find_docs: {sqlString}")
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    return full_set