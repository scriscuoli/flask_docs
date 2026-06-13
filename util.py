import bcrypt
import mysql.connector
import json
from pathlib import Path
import pymupdf
import sys

def password_hash(password: str, cost: int = 12) -> str:
    """
    Hash a password using bcrypt, compatible with PHP's password_hash().
    
    Args:
        password: The password to hash (string).
        cost: The cost factor for bcrypt (default 12, same as PHP's default).
    
    Returns:
        A bcrypt hash string compatible with PHP's password_hash().
    """
    # Ensure password is bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt and hash the password
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt(cost))
    # Return the hash as a string
    return hashed.decode('utf-8')

def password_verify(password: str, hashed_password: str) -> bool:
    """
    Verify a password against a bcrypt hash, compatible with PHP's password_verify().
    
    Args:
        password: The password to verify (string).
        hashed_password: The bcrypt hash to verify against (string).
    
    Returns:
        True if the password matches the hash, False otherwise.
    """
    try:
        # Ensure inputs are bytes
        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        # Verify the password against the hash
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    except (ValueError, TypeError):
        # Handle invalid hash formats or encoding issues
        return False
    


docs_db_config = {
    "host": "10.0.0.5",
    "database" : "docs",
    "user" : "docs",
    "passwd" : "!QAZ2wsx#EDC4rfv",
    "userTable": "user",
    "idColumn" : "uID",
    "userColumn": "userName",
    "passwordColumn": "password"
}

db_config =  {
    "docs": docs_db_config
}

dbname = "docs"


def db_connect(databaseName):
    config = db_config[databaseName]
    #print(config)
    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["passwd"],
        database=config["database"]
    )
    return connection

def getSiteName():
    return "Docs"

def get_pdf_file_date(inPdfFile:str):
    # mmddyyyyHHMMSS...
    stem = inPdfFile.rsplit('.', 1)[0]
    mm = stem[0:2]
    dd = stem[2:4]
    yyyy = stem[4:8]
    rtn  = {
        "year":f"{yyyy}",
        "month":f"{mm}",
        "day":f"{dd}"
        }
    return rtn
    

def pdf_image_pull(inPdfFile:str, outDir:str):
    doc = pymupdf.open(inPdfFile)
    ipath = Path(inPdfFile)
    opath = Path(outDir)
    stem = ipath.stem
    rtn = []
    for i, page in enumerate(doc):
        thumb_res = page.get_pixmap(matrix=pymupdf.Matrix(0.5, 0.5))
        thumb_fn = str(stem) + f"_{i+1}-thumb.png"
        thumb_path = opath / thumb_fn
        thumb_bytes = thumb_res.tobytes("png")   # in-memory, no disk write
        with open(thumb_path, "wb") as tf:
                tf.write(thumb_bytes)
        rtn.append({"page":i+1, "path":f"{thumb_fn}"})

    return rtn
