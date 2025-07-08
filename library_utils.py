def check_filepath():
    import os
    import requests
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        file_path = os.path.join(BASE_DIR, "docu.txt")
        if not os.path.exists(file_path):
            response = requests.get("https://raw.githubusercontent.com/ACSP-Tech/DATA-/refs/heads/main/docu.txt")
            if response.status_code == 200:
                with open(file_path, "x") as file:
                    file.write(response.text)
                print("Text file created and data written")
            else:
                print("failed to fetch the file from the URL")
        else:
            print("text file called docu.txt already exits")
            print()
        import json
        book_objects = []
        file_path1 = os.path.join(BASE_DIR, "book_record.json")
        if not os.path.exists(file_path1):
            with open(file_path, "r") as file:
                init_reading = file.readlines()
                for line in init_reading:
                    book_objects.append(line.strip().split("\t"))
            my_library = Library()
            for line in book_objects:
                with open(file_path1, "w") as file:
                    json.dump(book_objects, file)
                book_objects_record = Book(line[0], line[1], line[2])
                my_library.add_book(book_objects_record)
        else:
            print("json file called book_record already exits")
            print()

    except Exception as e:
        print(f"Error with the code: {e}")
    
        


def read_write_library_book_json():
    import json
    import os
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    book_objects = []
    file_path = os.path.join(BASE_DIR, "docu.txt")
    file_path1 = os.path.join(BASE_DIR, "book_record.json")
    if not os.path.exists(file_path1):
        with open(file_path, "r") as file:
            init_reading = file.readlines()
            for line in init_reading:
                book_objects.append(line.strip().split("\t"))
        my_library = Library()
        for line in book_objects:
            with open(file_path1, "w") as file:
                json.dump(book_objects, file)
            book_objects_record = Book(line[0], line[1], line[2])
            my_library.add_book(book_objects_record)
    else:
        my_library = Library()
        with open(file_path1, "r") as file:
            old_json = json.load(file)
        for line in old_json:
            book_objects_record = Book(line[0], line[1], line[2])
            my_library.add_book(book_objects_record)
    return my_library



def menu():
    print(".............................................................")
    print()
    print("...     Welcome to ACSP Management System              ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Add a new book", "Borrow a book", "Return a book", "View all books", "Save & Exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 5:
                print("Kindly choose from the option above")
                print()
                continue
            elif options < 1:
                print("Kindly choose from the option above")
                print()
                continue
            else:
                break
        except:
            print("Please Enter a valid Integer")
            print()
            continue
    return options

def add_option():
    import json
    import os
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "book_record.json")
    line0 = input("Enter the Book title: \n")
    line1 = input("Enter the Book author: \n")
    line2 = "available"
    book_objects1 = [line0, line1, line2]
    old_json = []
    with open(file_path, "r") as file:
        old_json = json.load(file)
    book_objects1 = [line0, line1, line2]
    old_json.append(book_objects1)
    with open(file_path, "w") as file:
        json.dump(old_json, file)
    my_library = Library()
    with open(file_path, "r") as file:
        old_json = json.load(file)
    for line in old_json:
        book_objects_record = Book(line[0], line[1], line[2])
        my_library.add_book(book_objects_record)
    print()
    print(f"{line0} by {line1} added sucessfully!")
    return my_library

def borrow_option():
    import json
    import os
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "book_record.json")
    my_library = Library()
    line0 = input("Enter the Book title: \n")
    line1 = input("Enter the Book author: \n")
    old_json = []
    with open(file_path, "r") as file:
        old_json = json.load(file)
    for book in old_json:
        if book[0] == line0 and book[1] == line1:
            if book[2] == "available":
                book[2] = "borrowed"
                with open(file_path, "w") as file:
                    json.dump(old_json, file)
                print(f"Book '{book[0]}' updated to borrowed on the database successfully.")
                my_library = Library()
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                for line in old_json:
                    book_objects_record = Book(line[0], line[1], line[2])
                    my_library.add_book(book_objects_record)
                print(f"{line0} by {line1} browwed sucessfully!")
                print()
            else:
                print("Book not available on the database")
                break
        else:
            print("inavild Book title and author name")
            break
    return my_library

def return_option():
    import json
    import os
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "book_record.json")
    my_library = Library()
    line0 = input("Enter the Book title: \n")
    line1 = input("Enter the Book author: \n")
    old_json = []
    with open(file_path, "r") as file:
        old_json = json.load(file)
    for book in old_json:
        if book[0] == line0 and book[1] == line1:
            if book[2] == "borrowed":
                book[2] = "available"
                with open(file_path, "w") as file:
                    json.dump(old_json, file)
                print(f"Book '{book[0]}' updated to available on the database successfully.")
                my_library = Library()
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                for line in old_json:
                    book_objects_record = Book(line[0], line[1], line[2])
                    my_library.add_book(book_objects_record)
                print(f"{line0} by {line1} returned sucessfully!")
                print()
                break
            else:
                print("Book is still available. hence, can't be returned")
                break
        else:
            print("inavild Book title and author name")
            break
    return my_library 

def view_option():
    import json
    import os
    from models import Library, Book
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "book_record.json")
    my_library = Library()
    with open(file_path, "r") as file:
        old_json = json.load(file)
    for line in old_json:
        book_objects_record = Book(line[0], line[1], line[2])
        my_library.add_book(book_objects_record)
    my_library.view_all_books()      