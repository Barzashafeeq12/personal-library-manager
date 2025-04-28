import streamlit as st
import json
import os

# File to store data
DATA_FILE = "library.txt"

# Load existing library
def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save the updated library
def save_library(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file)

# Add a new book
def add_book(library):
    st.subheader("Add a New Book")
    title = st.text_input('Enter the title of the book')
    author = st.text_input('Enter the author of the book')
    year = st.text_input('Enter the year of the book')
    genre = st.text_input('Enter the genre of the book')
    read = st.selectbox('Have you read this book?', ['Yes', 'No']) == "Yes"

    if st.button('Add Book'):
        new_book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read,
        }
        library.append(new_book)
        save_library(library)
        st.success(f'Book "{title}" added successfully!')

# Remove a book
def remove_book(library):
    st.subheader("Remove a Book")
    title_to_remove = st.text_input("Enter the title of the book to remove")
    
    if st.button('Remove Book'):
        initial_length = len(library)
        updated_library = [book for book in library if book['title'].lower() != title_to_remove.lower()]
        if len(updated_library) < initial_length:
            save_library(updated_library)
            st.success(f'Book "{title_to_remove}" removed successfully!')
        else:
            st.error(f'Book "{title_to_remove}" not found.')
        library.clear()
        library.extend(updated_library)

# Search the library
def search_library(library):
    st.subheader("Search the Library")
    search_by = st.selectbox('Search by', ['title', 'author'])
    search_term = st.text_input(f'Enter the {search_by}')
    
    if st.button('Search'):
        results = [book for book in library if search_term.lower() in book[search_by].lower()]
        if results:
            for book in results:
                status = "Read" if book['read'] else "Unread"
                st.write(f"📖 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - *{status}*")
        else:
            st.warning(f"No matching book found for '{search_term}' in {search_by}.")

# Display all books
def display_all_books(library):
    st.subheader("All Books")
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            st.write(f"📚 **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - *{status}*")
    else:
        st.info("Library is empty 🫥.")

# Show reading statistics
def display_statistics(library):
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    st.write(f"**Total books:** {total_books}")
    st.write(f"**Percentage of books read:** {percentage_read:.2f}%")

# Main app
def main():
    st.title("📚 Personal Book Library Manager")
    library = load_library()

    menu = ["Add Book", "Remove Book", "Search Library", "View All Books", "View Statistics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        add_book(library)
    elif choice == "Remove Book":
        remove_book(library)
    elif choice == "Search Library":
        search_library(library)
    elif choice == "View All Books":
        display_all_books(library)
    elif choice == "View Statistics":
        display_statistics(library)

if __name__ == '__main__':
    main()
