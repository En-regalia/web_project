from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import sqlite3
import os

#note: will need to impliment password hashing at a later date.
def initiliseDatabase(db_name):
    # check for database presence in the directory.
    if not os.path.exists(db_name):
        # if not found. Initally creates DB and creates table. 
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREAT TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
                password TEXT NOT NULL 
            )
        ''')
        print("Database "&db_name&" initated and table created sucessfuly")
    else:
        print("Database check completed"& db_name&" is present. Exiting function")



