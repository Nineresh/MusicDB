import sqlite3

"""CREATE TABLE IF NOT EXIST artist(
            

)"""

#conntar till en databas. Den tar in ett argument (string)
def connect():
    return sqlite3.connect("test_musicdatabase.db")
    

def createTable(connection):
    with connection:
        connection.execute()

def selectAll(connection):
    with connection:
        connection.execute()

def selectOne(connection, argument):
    with connection:
        connection.execute()

def commit_close():
    pass