CREATE DATABASE library_management;
USE library_management;

-- Table for books
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    publication_year INT,
    available_copies INT NOT NULL DEFAULT 1,
    CHECK (available_copies >= 0)
);

-- Table for members
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    join_date DATE NOT NULL
);

-- Table for borrowings
CREATE TABLE borrowings (
    borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Insert sample data into books
INSERT INTO books (title, author, isbn, publication_year, available_copies) VALUES
('To Kill a Mockingbird', 'Harper Lee', '9780446310789', 1960, 3),
('1984', 'George Orwell', '9780451524935', 1949, 2),
('Pride and Prejudice', 'Jane Austen', '9780141439518', 1813, 4);

-- Insert sample data into members
INSERT INTO members (first_name, last_name, email, join_date) VALUES
('John', 'Doe', 'john.doe@email.com', '2023-01-15'),
('Jane', 'Smith', 'jane.smith@email.com', '2023-02-20'),
('Alice', 'Johnson', 'alice.johnson@email.com', '2023-03-10');

-- Insert sample data into borrowings
INSERT INTO borrowings (book_id, member_id, borrow_date, return_date) VALUES
(1, 1, '2023-04-01', NULL),
(2, 2, '2023-04-05', '2023-04-12'),
(3, 3, '2023-04-10', NULL);