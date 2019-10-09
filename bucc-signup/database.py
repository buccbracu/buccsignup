import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def insert(conn, input):
    sql = "INSERT INTO signup(name, id, email, phone) VALUES(?, ?, ?, ?)"
    cur = conn.cursor()
    # Insert a row of data
    cur.execute(sql, input)
    # Save (commit) the changes
    conn.commit()
    

def query(input):
    database = "buccsignup.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        insert(conn, input)
    conn.close()
