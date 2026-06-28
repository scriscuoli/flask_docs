import util
import math
from decimal import *
from datetime import date, timedelta

dbname = util.dbname

    
def get_scanned(days_back:int):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT sf.*,pg.* FROM `scanned_files` sf, `pages` pg WHERE pg.sf_id = sf.sf_id and pg.sf_page_number = 1;"
    if days_back > 0:
        days_ago = date.today() - timedelta(days=days_back)
        formatted_date = days_ago.strftime("%Y-%m-%d")
        sqlString = f"SELECT sf.*,pg.* FROM `scanned_files` sf, `pages` pg WHERE sf.sf_creation_date > '{formatted_date}' and pg.sf_id = sf.sf_id and pg.sf_page_number = 1;"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    return myresult


def get_scanned_file_name(sf_id:int):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT sf.* FROM `scanned_files` sf WHERE sf.sf_id = {sf_id};"
    cursor.execute(sqlString)
    row = cursor.fetchone()
    return row['sf_path']
