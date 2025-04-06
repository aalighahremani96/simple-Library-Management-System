class Library1:
    def __init__(self):
        self.books = []

    def add_book(self,title,author):
        self.books.append({"title":title.lower(), "author":author.lower()})
        return print(f"book titled {title} by {author} was added!")
    
    def remove_book(self,title):
        for i in self.books:
            if title.lower() == i["title"]:
                self.books.remove(i)
                return print(f"Book titled '{title}' was removed!")
        print(f"Book titled '{title}' was not found!")
    
    def search_book(self,title):
        for i in self.books:
            if title.lower() == i["title"]:
                return print(f"book titled {title} exists and the author is {i["author"]}.")
        print(f"Book titled '{title}' was not found!")

    def show_books(self):
        for i in self.books:
            print(f"there is a book titled {i["title"]} and the author of the book is {i["author"]}.")


print(f"in module name is ({__name__})")
