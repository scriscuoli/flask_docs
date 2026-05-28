import bcrypt
import mysql.connector
import json

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

