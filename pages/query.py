import util
import math
from decimal import *
from datetime import date, timedelta
from documents.query import create_document
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
    
def get_pids_for_pages(sf_id:int, pages:list):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    # SELECT pg_id FROM `pages` WHERE sf_id = 2 and sf_page_number in (1,2,3);
    pgs = ",".join(map(str, pages))
    sqlString = f"SELECT pg_id FROM `pages` WHERE sf_id = {sf_id} and sf_page_number in ({pgs});"
    print(f"get_pids_for_pages: {sqlString}")
    cursor.execute(sqlString)
    full_set = cursor.fetchall()
    return full_set

def create_document_page_entry(dc_id:int, pg_id:int):
    connection = util.db_connect(dbname)
    cursor = connection.cursor(dictionary=True)
    sqlString = f"insert into document_page (dc_id,pg_id) values ('{dc_id}','{pg_id}');"
    #print(sqlString)
    
    cursor.execute(sqlString)
    dc_id = cursor.lastrowid
    connection.commit()
    return dc_id

def create_document_from_spec(sf_id:int, dc_name:str, dc_date:str, specs:list):
    print(f"create_document_from_spec: {sf_id}  {dc_name}  {dc_date}")
    print(specs)
    dc_id = create_document(dc_name,dc_date)
    rows = get_pids_for_pages(sf_id,specs)
    for row in rows:
        pg_id = row['pg_id']
        create_document_page_entry(dc_id,pg_id)

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

