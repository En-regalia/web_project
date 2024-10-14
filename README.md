# Family Chores Tracker
This is an academic project aimed at building a full-stack application for tracking family chores. The application is built without the use of frameworks, using vanilla HTML, CSS, and JavaScript for the front end, Python's built-in HTTP server for the backend, and SQLite for the database. The main objective of this project is to enable users (family members) to log in and track their assigned chores through a simple web interface.

## Table of Contents
- Project Overview
- Technology Stack
- Installation
- Features
- User Stories
- Usage
- File Structure
- Setting up AWS VPC
- Database Schema
- Contributing
- License

## Project Overview
The Family Chores Tracker allows users to:

Create accounts and log in with a username and hashed password.
View all chores assigned to all users but only update the status of chores they are personally assigned.
Track the completion of chores.
Update and delete chores as needed (within permission boundaries).
The goal of this project is to develop a fully functional web application without the use of any frameworks (e.g., no React, Django, Flask). The server runs on AWS within a VPC and uses Python's built-in HTTP server capabilities. All user and chore data is stored locally in a SQLite database.

## Technology Stack
### Front End:
HTML5: Markup language for structuring the application.
CSS3: For styling the web pages.
JavaScript: Provides interactivity, validation, and dynamic updates.

### Back End:
Python: Using the built-in HTTP server to handle requests.
AWS: Server hosted on AWS using VPC for network isolation.

### Database:
SQLite: A lightweight, file-based relational database to store user and chore data.
Security:
Password Hashing: User passwords are securely stored using hashing (e.g., via Python's hashlib or bcrypt).

### Other:
No Frameworks: This project is built from scratch without any frameworks to provide a learning opportunity for understanding core concepts.


## Installation
To run the Family Chores Tracker locally, follow these steps:

Clone the repository:

```bash
git clone https://github.com/En-regalia/web_project.git
```
Navigate to the project directory:

```bash
cd web_project
```
Set up a virtual environment:

```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies (If there are any external packages, though currently not expected since no frameworks are used):

```bash

pip install -r requirements.txt
```

Start the Python HTTP server:

```bash
Copy code
python server.py
```

Access the application by opening a web browser and going to:

```arduino
http://localhost:8000
```
## Features
- User authentication with hashed passwords (login, registration).
- View all chores in the system, but only update completion status of chores assigned to the logged-in user.
- Add and assign chores to users.
- Mark chores as completed.
- Edit or delete existing chores (only if assigned or created by the user).

More features could be added as the project evolves.

## User Stories
(Placeholder for user stories. Will be added later.)

## Usage

### Frontend
All frontend files are located in the /public directory.
HTML, CSS, and JavaScript handle the user interface and communicate with the server using fetch API calls.

### Backend
The backend server is written in Python using the built-in http.server library.
The server handles routing, requests, and responses.
Passwords are stored securely in the database using password hashing.
Requests are handled via GET, POST, PUT, and DELETE methods, which communicate with the SQLite database.

### Database
The SQLite database stores user information (with hashed passwords) and chore data.
The database file is created automatically when the server starts if it does not already exist.
File Structure
```bash

├── /public
│   ├── style.css        # CSS for styling the pages
│   ├── app.js           # JavaScript for frontend functionality
├── /Database
│   └── chores.db        # SQLite database file (auto-generated)
├── index.html           # Main frontend page
├── server.py            # Python backend server
├── README.md            # This README file
└── requirements.txt     # (Optional) Any dependencies (none currently)
```

Setting up AWS VPC
To deploy the Family Chores Tracker on AWS using a Virtual Private Cloud (VPC), follow the generic steps below:

1. Set up an AWS EC2 instance
- Login to AWS Console and navigate to the EC2 Dashboard.
- Launch a new EC2 instance with an appropriate AMI (Amazon Machine Image) such as Ubuntu Server.
- Configure security groups to allow HTTP (port 80) and SSH (port 22) access.
- Allocate and associate an Elastic IP to ensure the server has a static public IP address.

2. SSH into your EC2 instance
- Once your EC2 instance is running, SSH into it using the following command:

```bash
ssh -i /path/to/your-key.pem ubuntu@your-ec2-public-ip
```
Replace /path/to/your-key.pem with the path to your private SSH key file and your-ec2-public-ip with the public IP of your instance.

3. Transfer server files to your EC2 instance
To transfer the server.py file and other necessary files to your EC2 instance, use the scp command:

```bash
scp -i /path/to/your-key.pem server.py ubuntu@your-ec2-public-ip:/home/ubuntu/
```
This will copy the server.py file to the home directory of your EC2 instance.

4. Start the server
Once you've transferred the necessary files, SSH into the EC2 instance and run the Python HTTP server:

```bash
python3 server.py
```

You can now access your application from the browser using your EC2 instance's public IP.

## Database Schema
(Placeholder for the database schema. To be decided later.)

## Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes.
Submit a pull request for review.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
