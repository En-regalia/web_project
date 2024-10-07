from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import sqlite3
import os

#note: will need to impliment password hashing at a later date. (bcrypt)
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
        conn.close()
    else:
        print("Database check completed"& db_name&" is present. Exiting function")


class RequestHandler(BaseHTTPRequestHandler):

    def do_get(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        initiliseDatabase("users.db")
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        if "email" in query_params:
            email = query_params['email'][0]

            cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            result = cursor.fetchone()

            user_id = result[0]

            response = f"User ID for the email {email} is: {user_id}"

            if response:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(response.encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"User not found for the provided email")
            
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bad request: Missing email")
        


