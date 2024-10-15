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
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL 
            )
        ''')
        print("Database " + db_name + " initated and table created sucessfuly")
        conn.close()
    else:
        print("Database check completed" + db_name + " is present. Exiting function")


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        #Parsed the URL and extracted query parameters from the incoming GET request 
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

           

        #Logic to check which responce to give. 
        if "email" in query_params:
            #Handle email querie defined below
            handle_email_query(query_params)
        elif self.path == "/":
            self.handle_home()
            print("Sending home page")
        else:
            self.handel_error()
            print("Sending Error page")
        
        #searches for the user's email in the database using the entered email as the query and returns the user_ID
    def handle_email_query(self, query_params):
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            email = query_params['email'][0]

            cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                response = f"User ID for the email {email} is: {user_id}"
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"User not found for the provided email")

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
            conn.close()
    
    def handle_home(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow requests from any domain
        self.end_headers()
        
        html_content = """<div class = "card">
                <ul class="switch-list">
                    <h2>Felicia's list</h2>
                    <li>
                        <label class="switch">
                            <input type="checkbox">
                            <span class="slider"></span>
                        </label>
                        <span class="slider-text">Chore 1</span>
                    </li>
                    <li>
                        <label class="switch">
                            <input type="checkbox">
                            <span class="slider"></span>
                        </label>
                        <span class="slider-text">Chore 2</span>
                    </li>
                    <li>
                        <label class="switch">
                            <input type="checkbox">
                            <span class="slider"></span>
                        </label>
                        <span class="slider-text">Chore 3</span>
                    </li>
                    <li>
                        <label class="switch">
                            <input type="checkbox">
                            <span class="slider"></span>
                        </label>
                        <span class="slider-text">Chore 4</span>
                    </li>
                </ul>
            </div>"""

        self.wfile.write(html_content.encode('utf-8'))


    #baisc error handle in case of path error.
    def handle_error(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Bad request: Page not found")

#block to define the server
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)  # Serve on all available interfaces at port 8000
    httpd = server_class(server_address, handler_class)
    print('Starting server... ready for requests')
    initiliseDatabase("users.db")
    httpd.serve_forever()  # Start serving requests

if __name__ == '__main__':
    run()
