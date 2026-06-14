import util
import math
from decimal import *
from datetime import date, timedelta

dbname = util.dbname

    
def get_pages_for_scanned_file(sf_id:int, index_only=True):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"SELECT pg.* FROM `pages` pg WHERE pg.sf_id = {sf_id};"
    #print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    if index_only:
        indices = []
        for row in full_set:
            indices.append(row['pg_id'])
        return indices
    else:
        return full_set

def get_undocumented_pages_for_scanned_file(sf_id:int):
    rtn = []
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    upl = get_pages_for_scanned_file(sf_id,True)
    sqlString = "SELECT ids.pg_id, COUNT(dp.pg_id) AS cnt FROM ( "
    pre = "SELECT "
    post = " AS pg_id "
    for pg_id in upl:
        sqlString = sqlString + f"{pre} {pg_id} {post}"
        pre = "UNION ALL SELECT "
        post = ""
    sqlString = sqlString + ") AS ids LEFT JOIN document_page dp ON dp.pg_id = ids.pg_id GROUP BY ids.pg_id;"
    #print(sqlString)
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    for row in full_set:
        if row['cnt'] == 0:
            rtn.append(row['pg_id'])
    return rtn

