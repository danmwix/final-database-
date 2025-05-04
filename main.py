from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'database': 'library_management'
}

# Pydantic model for Book
class Book(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int | None = None
    available_copies: int = 1

# Function to get database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

# CREATE: Add a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO books (title, author, isbn, publication_year, available_copies)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (book.title, book.author, book.isbn, book.publication_year, book.available_copies)
        cursor.execute(query, values)
        connection.commit()
        return book
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error creating book: {e}")
    finally:
        cursor.close()
        connection.close()

# READ: Get all books
@app.get("/books/")
def get_all_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return books
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving books: {e}")
    finally:
        cursor.close()
        connection.close()

# READ: Get a book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
        book = cursor.fetchone()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book: {e}")
    finally:
        cursor.close()
        connection.close()

# UPDATE: Update a book by ID
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        UPDATE books
        SET title = %s, author = %s, isbn = %s, publication_year = %s, available_copies = %s
        WHERE book_id = %s
        """
        values = (book.title, book.author, book.isbn, book.publication_year, book.available_copies, book_id)
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        connection.commit()
        return book
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error updating book: {e}")
    finally:
        cursor.close()
        connection.close()

# DELETE: Delete a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        connection.commit()
        return {"message": "Book deleted successfully"}
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error deleting book: {e}")
    finally:
        cursor.close()
        connection.close()