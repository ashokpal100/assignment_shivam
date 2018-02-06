import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "2016",
                           db = "pal_db")
    c = conn.cursor()

    return c, conn
