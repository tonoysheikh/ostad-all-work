import json

book_list = []
lent_list = []

def load_data():
    global book_list, lent_list
    try:
        with open('library_data.json', 'r') as file:
            data = json.load(file)
            book_list = data.get('books', [])
            lent_list = data.get('lent_books', [])
    except FileNotFoundError:
        pass

def save_data():
    data = {
        'books': book_list,
        'lent_books': lent_list
    }
    with open('library_data.json', 'w') as file:
        json.dump(data, file)

def add_book():
    book = {}
    book["title"] = input("Enter the title of the book: ")
    book["author"] = input("Enter the author(s) of the book (comma separated): ").split(',')
    book["ISBN"] = input("Enter the ISBN of the book: ")
    book["year"] = int(input("Enter the year of the book: "))
    book["price"] = int(input("Enter the price of the book: "))
    book["quantity"] = int(input("Enter the quantity of the book: "))
    book_list.append(book)
    save_data()
    print("Book added successfully!\n")

def view_all_books():
    print("Books available: \n")
    for book in book_list:
        print(f"Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")

def search_books():
    item = input("Search by:\n1. Book Title\n2. Book ISBN\n3. Book Author\nEnter your choice: ")

    if item == "1":
        search = input("Enter the book title: ")
        for book in book_list:
            if search.lower() in book["title"].lower():
                print(f"Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "2":
        search = input("Enter the book ISBN: ")
        for book in book_list:
            if search == book["ISBN"]:
                print(f"Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "3":
        search = input("Enter the book author: ")
        for book in book_list:
            if any(search.lower() in author.lower() for author in book["author"]):
                print(f"Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    else:
        print("Invalid input")

def remove_book():
    item = input("Search to remove by:\n1. Book Title\n2. Book ISBN\n3. Book Author\nEnter your choice: ")

    if item == "1":
        search = input("Enter the book title: ")
        for index, book in enumerate(book_list):
            if search.lower() in book["title"].lower():
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "2":
        search = input("Enter the book ISBN: ")
        for index, book in enumerate(book_list):
            if search == book["ISBN"]:
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "3":
        search = input("Enter the book author: ")
        for index, book in enumerate(book_list):
            if any(search.lower() in author.lower() for author in book["author"]):
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    else:
        print("Invalid input")
        return

    remove_index = int(input("Enter the number of the book to remove: ")) - 1
    if 0 <= remove_index < len(book_list):
        book_list.pop(remove_index)
        save_data()
        print("Book successfully removed.")
    else:
        print("Invalid index.")

def lent_book():
    item = input("Search to lend by:\n1. Book Title\n2. Book ISBN\n3. Book Author\nEnter your choice: ")

    if item == "1":
        search = input("Enter the book title: ")
        for index, book in enumerate(book_list):
            if search.lower() in book["title"].lower():
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "2":
        search = input("Enter the book ISBN: ")
        for index, book in enumerate(book_list):
            if search == book["ISBN"]:
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    elif item == "3":
        search = input("Enter the book author: ")
        for index, book in enumerate(book_list):
            if any(search.lower() in author.lower() for author in book["author"]):
                print(f"{index+1}. Book Title: {book['title']}\nBook Author(s): {', '.join(book['author'])}\nBook ISBN: {book['ISBN']}\nPublishing Year: {book['year']}\nPrice: {book['price']}\nQuantity: {book['quantity']}\n")
    else:
        print("Invalid choice")
        return

    lent_index = int(input("Enter the index of the book to lend: ")) - 1
    if 0 <= lent_index < len(book_list):
        numberOfBooks = int(input("How many books do you want to lend: "))
        if numberOfBooks <= book_list[lent_index]["quantity"]:
            name = input("Enter your name: ")
            sId = input("Enter your student ID: ")
            lent_list.append({
                "name": name,
                "student_id": sId,
                "book_ISBN": book_list[lent_index]["ISBN"],
                "quantity": numberOfBooks
            })
            book_list[lent_index]["quantity"] -= numberOfBooks
            save_data()
            print(f"Hello, {name}.\n{numberOfBooks} book(s) successfully lent.")
        else:
            print("Not enough books available to lend")
    else:
        print("Invalid index")

def view_lent_list():
    print("List of all borrowers: \n")
    for item in lent_list:
        print(f"Name: {item['name']}\nStudent ID: {item['student_id']}\nBook ISBN: {item['book_ISBN']}\nQuantity: {item['quantity']}\n")

def return_lent_book():
    sId = input("Enter your student ID: ")
    return_list = [item for item in lent_list if item["student_id"] == sId]
    
    if return_list:
        print("Books you have borrowed: \n")
        for index, item in enumerate(return_list):
            print(f"{index+1}. Book ISBN: {item['book_ISBN']}\nQuantity: {item['quantity']}\n")
        
        return_index = int(input("Enter the number of index to return: ")) - 1
        if 0 <= return_index < len(return_list):
            numberOfBooks = int(input("How many books do you want to return: "))
            if numberOfBooks <= return_list[return_index]["quantity"]:
                book_ISBN = return_list[return_index]["book_ISBN"]
                for book in book_list:
                    if book["ISBN"] == book_ISBN:
                        book["quantity"] += numberOfBooks
                        break
                
                return_list[return_index]["quantity"] -= numberOfBooks
                if return_list[return_index]["quantity"] == 0:
                    lent_list.remove(return_list[return_index])
                save_data()
                print(f"{numberOfBooks} book(s) successfully returned.")
            else:
                print("Invalid number of books")
        else:
            print("Invalid index")
    else:
        print("No books found for your student ID.")

load_data()

while True:
    print("-----------------------------------------\n")
    print("Welcome to the Library Management System\n")
    print("-----------------------------------------\n")
    print("Menu :\n")
    menu = """
    1. Add new book
    2. View all books
    3. Search for a book
    4. Remove a book
    5. Lend book
    6. View full list of lent books
    7. Return book
    8. Exit
    """
    print(menu)
    
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_book()
    elif ch == 2:
        view_all_books()
    elif ch == 3:
        search_books()
    elif ch == 4:
        remove_book()
    elif ch == 5:
        lent_book()
    elif ch == 6:
        view_lent_list()
    elif ch == 7:
        return_lent_book()
    elif ch == 8:
        save_data()
        break
    else:
        print("Invalid choice")
