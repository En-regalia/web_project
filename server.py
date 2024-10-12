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
        
        #Parsed the URL and extracted query parameters from the incoming GET request 
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        #initalised and coonectioned 
        initiliseDatabase("users.db")
    

        #Logic to check which responce to give. 
        if "email" in query_params:
            #Handel email querie defined below
            handel_email_query(query_params)
        elif self.path == "/":
            self.handel_home()
        else:
            self.handel_error()
        
        #searches for the user's email in the database using the entered email as the query and returns the user_ID
        def handel_email_query(self, query_params):
            try:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
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
        
            finally:
                conn.close
        
        def handel_home(self):
            #HOLD WORKING ON PAGE TEMPLATE IN ORDER TO INCLUDEIN HANDELER.
            print("HOLD_CODE error on line 79")

        #baisc error handle in case of path error.
        def handel_error(self):
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bad request: Page not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make it publicly accessible
