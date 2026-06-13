from util import dbname,db_connect,get_pdf_file_date
import math
from decimal import *
from datetime import datetime



def add_pdf_to_db(pdf_file:str):
    sfID = 0
    connection = db_connect(dbname)
    #current_date = datetime.now().strftime("%Y-%m-%d")
    ymd = get_pdf_file_date(pdf_file)
    current_date = f"{ymd["year"]}-{ymd["month"]}-{ymd["day"]}"
    cursor = connection.cursor(dictionary=True)
    sqlString = f"insert into scanned_files (sf_path,sf_creation_date) values ('{pdf_file}','{current_date}');"
    print(sqlString)
    
    cursor.execute(sqlString)
    sfID = cursor.lastrowid
    connection.commit()
    return sfID

def add_thumbnails_to_db(sf_id:int, thumbnails:list):
    connection = db_connect(dbname)
    pg_date = datetime.now().strftime("%Y-%m-%d")
    cursor = connection.cursor(dictionary=True)
    sqlString = "insert into pages (sf_id,pg_path,pg_date,sf_page_number) values "
    sep = ""
    for thumbnail in thumbnails:
        sf_page_number = thumbnail["page"]
        pg_path = thumbnail["path"]
        sqlString = sqlString + sep + f"({sf_id},'{pg_path}','{pg_date}',{sf_page_number})"
        sep = ","
    #print(sqlString)
    cursor.execute(sqlString)
    connection.commit()
    return 
    
