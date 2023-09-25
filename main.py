import sqlite3


# Define function to add new book
def add_new_book(conn, book_id, title, author, isbn, status="Available"):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (BookID, Title, Author, ISBN, Status) VALUES (?, ?, ?, ?, ?)",
                   (book_id, title, author, isbn, status))
    conn.commit()


# Define function to find book details by BookID
def find_book_by_id(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE BookID = ?", (book_id,))
    return cursor.fetchone()


# Define function to find book reservation status by multiple conditions
def find_book_reservation_status(conn, query_text):
    cursor = conn.cursor()
    if query_text.startswith("LB"):
        cursor.execute("SELECT * FROM Reservations WHERE BookID = ?", (query_text,))
    elif query_text.startswith("LU"):
        cursor.execute("SELECT * FROM Reservations WHERE UserID = ?", (query_text,))
    elif query_text.startswith("LR"):
        cursor.execute("SELECT * FROM Reservations WHERE ReservationID = ?", (query_text,))
    else:
        cursor.execute("SELECT * FROM Books WHERE Title = ?", (query_text,))
    return cursor.fetchall()


# Define function to find all books in the database
def find_all_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    return cursor.fetchall()


# Define function to update book details by BookID
def update_book_details(conn, book_id, title=None, author=None, isbn=None, status=None):
    cursor = conn.cursor()
    if title:
        cursor.execute("UPDATE Books SET Title = ? WHERE BookID = ?", (title, book_id))
    if author:
        cursor.execute("UPDATE Books SET Author = ? WHERE BookID = ?", (author, book_id))
    if isbn:
        cursor.execute("UPDATE Books SET ISBN = ? WHERE BookID = ?", (isbn, book_id))
    if status:
        cursor.execute("UPDATE Books SET Status = ? WHERE BookID = ?", (status, book_id))
    conn.commit()


# Define function to delete book by BookID
def delete_book_by_id(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Reservations WHERE BookID = ?", (book_id,))
    cursor.execute("DELETE FROM Books WHERE BookID = ?", (book_id,))
    conn.commit()


# Main program and user interface
def main():
    conn = sqlite3.connect("library_management_system.db")

    while True:
        print("Library Management System")
        print("1. Add a new book")
        print("2. Find a book's detail by BookID")
        print("3. Find a book's reservation status")
        print("4. Find all books")
        print("5. Modify/update book details")
        print("6. Delete a book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter BookID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            add_new_book(conn, book_id, title, author, isbn)
        elif choice == "2":
            book_id = input("Enter BookID: ")
            print(find_book_by_id(conn, book_id))
        elif choice == "3":
            query_text = input("Enter BookID, Title, UserID, or ReservationID: ")
            print(find_book_reservation_status(conn, query_text))
        elif choice == "4":
            print(find_all_books(conn))
        elif choice == "5":
            book_id = input("Enter BookID: ")
            title = input("Enter new Title (leave empty if no change): ")
            author = input("Enter new Author (leave empty if no change): ")
            isbn = input("Enter new ISBN (leave empty if no change): ")
            status = input("Enter new Status (leave empty if no change): ")
            update_book_details(conn, book_id, title, author, isbn, status)
        elif choice == "6":
            book_id = input("Enter BookID: ")
            delete_book_by_id(conn, book_id)
        elif choice == "7":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()