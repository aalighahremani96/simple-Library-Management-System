# Library Management System 📚

This project is part of my Python course assignments. It focuses on working with Modules, Packages, and creating installable Python packages using `pip` and `PyPI` standards.

---

## Project Description
A library wants to develop a system for managing its books. This system should provide features like:

- Adding a book  
- Removing a book  
- Searching for a book  
- Displaying all books  

You need to implement this system in a modular way and prepare the package for local installation using `pip`.

---

## Tasks

### 1. Using Modules and Packages
#### Task:
- Create a module named `library.py` containing a class `Library` with the following features:

##### Attributes:
- A list to store books.

##### Methods:
- `add_book(title, author)` — Adds a new book to the list.  
- `remove_book(title)` — Removes a book from the list by its title.  
- `search_book(title)` — Searches for a book by its title.  
- `show_books()` — Displays all the books in the library.

---

### 2. Using `__name__ == "__main__"`
#### Task:
- Create a new file called `main.py` that imports and uses `library.py`.
- Check if `main.py` is being executed directly.
- If so, display a simple menu allowing the user to:
  - Add a book  
  - Remove a book  
  - Search for a book  
  - Show all books  

---

### 3. Converting the Module to an Installable Package
#### Task:
- Prepare your project for local installation:

##### Steps:
1. Create a folder called `mylibrary/` and place `library.py` inside it.
2. Add an empty `__init__.py` file inside `mylibrary/`.
3. Create a `setup.py` file for package installation.

##### Installation:
- Run the following command in your terminal to install the package locally:
```bash
pip install .
