import sqlite3
from sqlite3 import Error
 
class SqliteHandler:

    def create_connection(self,db_file):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            conn.close()
    
