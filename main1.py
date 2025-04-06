from mylibrary1.library1 import Library1



def main1():
    library1 = Library1()
    
    while True:
        print("!!! library1 system !!!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Show all books")
        print("5. Exit")
        
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library1.add_book(title, author)
        
        elif choice == 2:
            title = input("Enter title of the book to remove: ")
            library1.remove_book(title)
        
        elif choice == 3:
            title = input("Enter title to search: ")
            library1.search_book(title)
        
        elif choice == 4:
            library1.show_books()
        
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    print(f"in main program name is ({__name__})")
    main1()