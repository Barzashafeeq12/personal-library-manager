import json
import os
Data_file ="library.txt"
def load_library():
    if os.path.exists(Data_file):
        with open(Data_file,"r") as file:
            return json.load(file)
        return[]
def save_library(library):
    with open(Data_file,"w") as file:
        json.dump(library,file)

def add_book(library):
    title =input('Enter the title of the book:')
    author =input('Enter the author of the book:')
    year =input('Enter the year of the book:')
    genre =input('Enter the genre of the book:')
    read =input('Have you read this book? (Yes/No):').lower() == "Yes"

    new_book ={
        'title':title,
        'auther':author,
        'year':year,
        'genre':genre,
         'read':read,
    }
    library.append(new_book)
    save_library(library)
    print(f'Book {title} added sucessfully.')
def remove_book(library):
    title =input("Enter the title book to remove from library")
    initial_length =len(library)
    library =[book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book {title} removed sucessfully.') 
    else:
         print(f'Book {title} is not founded.') 
def search_library(library):
    search_by =input("Search by author or Book").lower()
    search_term =input(f'Enter the{search_by}')  
    results =[book for book in library if search_term in book[search_by].lower()]

    if results :
        for book in results:
            status ="Read" if book['read'] else "Unread" 
            print(f"{book['title']} by {book['author']} - {book['year']} -{book['genre']} - {status}")
    else:
        print(f"No matching book is founded {search_term} in {search_by} field.")
def display_all_books(library):
    if(library):
        for book in library:
            status ="Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} -{book['genre']} - {status}")
    else:
        print("Library is empty🫥.")
def display_statistics(library):
            total_books =len(library)
            read_books =len([book for book in library if book['read']])
            percentage_read =(read_books / total_books) *100 if total_books > 0 else 0
            print (f'Total books:{total_books}')
            print(f'Precentage of read books is :{percentage_read:.2f}%')
def main():
     library =load_library()
     while True:
          print("Welcome to your personal book library👏🏻👏🏻")
          print("Menu")
          print("1. Add book")
          print("2. Remove book")
          print("3. Search the related library")
          print("4. All books")
          print("5. Display statistics")
          print("6. Exit")

          choice = input("Choose your option")
          if choice == '1':
            add_book(library)
          elif choice == '2':
            remove_book(library)     
          elif choice == '3':
           search_library(library)
          elif choice == '4':
           display_all_books(library)
          elif choice == '5':
           display_statistics(library)
          elif choice == '6':
             print("ByeByee👋🏻")
             break
          else:
              print("Invalid option.Try again")
if __name__ == '__main__':
    main()             



