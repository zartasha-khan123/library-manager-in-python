import streamlit as st
import database  # Import MySQL functions

st.title("📚 Personal Library Manager")

# Sidebar Menu
menu = st.sidebar.selectbox("Navigation", ["Add Book", "Remove Book", "Search Book", "Display All Books", "Statistics"])

# Add Book
if menu == "Add Book":
    st.header("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        database.add_book(title, author, int(year), genre, read_status)
        st.success(f"📖 '{title}' added successfully!")

# Remove Book
elif menu == "Remove Book":
    st.header("❌ Remove a Book")
    books = database.get_all_books()
    book_titles = {book["title"]: book["id"] for book in books}

    if book_titles:
        book_to_remove = st.selectbox("Select a book to remove", book_titles.keys())

        if st.button("Remove Book"):
            database.remove_book(book_titles[book_to_remove])
            st.success(f"🗑️ '{book_to_remove}' removed successfully!")
    else:
        st.warning("⚠️ No books available to remove!")

# Search Book
elif menu == "Search Book":
    st.header("🔎 Search a Book")
    search_query = st.text_input("Enter book title or author")

    if st.button("Search"):
        books = database.search_book(search_query)
        if books:
            for book in books:
                status = "✅ Read" if book["read_status"] else "❌ Unread"
                st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
        else:
            st.warning("🚫 No books found!")

# Display All Books
elif menu == "Display All Books":
    st.header("📚 Your Library")
    books = database.get_all_books()

    if books:
        for book in books:
            status = "✅ Read" if book["read_status"] else "❌ Unread"
            st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
    else:
        st.info("📭 Your library is empty!")

# Statistics
elif menu == "Statistics":
    st.header("📊 Library Statistics")
    total_books, read_books, unread_books = database.get_statistics()

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books}")
    st.write(f"❌ **Books Unread:** {unread_books}")

st.sidebar.write("---")
st.sidebar.write("Built with ❤️ using Streamlit & MySQL")
