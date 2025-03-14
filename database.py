import mysql.connector

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # <-- Replace with your MySQL username if different
        password="mysons2830",  # <-- Replace with your MySQL password
        database="library_db"
    )

# Add Book
def add_book(title, author, year, genre, read_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO books (title, author, year, genre, read_status) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, author, year, genre, read_status))
    conn.commit()
    conn.close()

# Remove Book
def remove_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    conn.commit()
    conn.close()

# Fetch All Books
def get_all_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

# Search Book
def search_book(query):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    search_query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(search_query, (f"%{query}%", f"%{query}%"))
    books = cursor.fetchall()
    conn.close()
    return books

# Get Statistics
def get_statistics():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = 1")
    read_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = 0")
    unread_books = cursor.fetchone()[0]

    conn.close()
    return total_books, read_books, unread_books
