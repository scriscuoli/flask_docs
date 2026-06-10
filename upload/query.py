import util
import math
from decimal import *
from datetime import datetime

dbname = util.dbname

def add_pdf_to_db(pdf_file:str):
    sfID = 0
    connection = util.db_connect(dbname)
    current_date = datetime.now().strftime("%Y-%m-%d")
    cursor = connection.cursor(dictionary=True)
    sqlString = f"insert into scanned_files (path,creation_date) values ('{pdf_file}','{current_date}');"
    print(sqlString)
    
    cursor.execute(sqlString)
    sfID = cursor.lastrowid
    connection.commit()
    return sfID

def add_thumbnails_to_db(sfID:int, thumbnails:list):
    connection = util.db_connect(dbname)
    current_date = datetime.now().strftime("%Y-%m-%d")
    cursor = connection.cursor(dictionary=True)
    sqlString = "insert into pages (sfID,path,date,sf_page_number) values "
    sep = ""
    for thumbnail in thumbnails:
        sf_page_number = thumbnail["page"]
        path = thumbnail["path"]
        sqlString = sqlString + sep + f"({sfID},'{path}','{current_date}',{sf_page_number})"
        sep = ","
    #print(sqlString)
    cursor.execute(sqlString)
    connection.commit()
    return 
    
