# final-database-
Library Management System API
This project implements a MySQL database and a FastAPI-based CRUD API for a Library Management System. The system manages books, members, and borrowings, with the API focusing on CRUD operations for the books table.
Prerequisites

MySQL: Version 8.0 or higher, with a running server.
Python: Version 3.8 or higher.
VS Code: Recommended for editing and running the code.
Git (optional): For cloning or managing the project.

Setup Instructions
1. Clone or Download the Project

If using Git, clone the repository:git clone <repository-url>


Alternatively, download the project files (library_management.sql, main.py) and place them in a project folder.

2. Set Up MySQL Database

Install MySQL (if not already installed):
Download from mysql.com and follow the installation instructions for your OS.


Run the SQL File:
Open MySQL Workbench or a MySQL command-line client.
Log in with your MySQL credentials (e.g., mysql -u root -p).
Execute the library_management.sql file:SOURCE path/to/library_management.sql;


This creates the library_management database, tables (books, members, borrowings), and inserts sample data.


Verify Database:
Run the following queries to confirm:USE library_management;
SELECT * FROM books;
SELECT * FROM members;
SELECT * FROM borrowings;





3. Set Up Python Environment

Create a Virtual Environment:
Open a terminal in VS Code (Ctrl+`) in your project folder.
Create and activate a virtual environment:
Windows:python -m venv .venv
.venv\Scripts\activate


Mac/Linux:python -m venv .venv
source .venv/bin/activate






Install Dependencies:
With the virtual environment activated, install required packages:pip install fastapi uvicorn mysql-connector-python pydantic





4. Configure the API

Update MySQL Credentials:
Open main.py in VS Code.
Update the db_config dictionary with your MySQL credentials:db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'database': 'library_management'
}


Ensure the host and database match your MySQL setup.



5. Run the API

Start the FastAPI Server:
In the terminal (with the virtual environment activated), run:uvicorn main:app --reload


This starts the server at http://127.0.0.1:8000.


Test the API:
Open a browser and visit http://127.0.0.1:8000/docs to access the Swagger UI.
Use the Swagger UI to test the following endpoints:
POST /books/: Create a new book (e.g., { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "9780743273565", "publication_year": 1925, "available_copies": 2 }).
GET /books/: Retrieve all books.
GET /books/{book_id}: Retrieve a book by ID.
PUT /books/{book_id}: Update a book by ID.
DELETE /books/{book_id}: Delete a book by ID.


Alternatively, use Postman or curl to send requests.



6. Verify Database Changes

After testing the API, check the books table in MySQL to confirm CRUD operations:SELECT * FROM books;



Troubleshooting

MySQL Connection Error:
Ensure MySQL is running (mysql -u root -p).
Verify the user, password, host, and database in main.py.


ModuleNotFoundError:
Confirm the virtual environment is activated and dependencies are installed (pip list).
Reinstall dependencies if needed: pip install fastapi uvicorn mysql-connector-python pydantic.


Uvicorn Not Found:
Install uvicorn: pip install uvicorn.


API Errors:
Check the terminal for error messages (e.g., database connection issues).
Ensure the library_management database and books table exist.



Project Structure

library_management.sql: SQL file to create the database and tables.
main.py: FastAPI application implementing CRUD operations for the books table.

Notes

The API focuses on the books table for simplicity. You can extend it to include members and borrowings by adding similar endpoints.
Tested on Python 3.10, MySQL 8.0, and FastAPI 0.104.1.
For production, secure the MySQL credentials (e.g., use environment variables) and deploy with a production server (not --reload).

