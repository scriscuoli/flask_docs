import util
import math
from decimal import *
from datetime import datetime

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