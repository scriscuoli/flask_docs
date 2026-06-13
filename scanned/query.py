import util
import math
from decimal import *
from datetime import date, timedelta

dbname = util.dbname

    
def get_scanned():
    connection = util.db_connect(dbname)
    date_60_days_ago = date.today() - timedelta(days=60)
    formatted_date = date_60_days_ago.strftime("%Y-%m-%d")
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT sf.*,pg.* FROM `scanned_files` sf, `pages` pg WHERE sf.sf_creation_date > '{formatted_date}' and pg.sf_id = sf.sf_id and pg.sf_page_number = 1;"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    myresult = cursor.fetchall()
    return myresult
