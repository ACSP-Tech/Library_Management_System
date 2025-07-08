class Book:
    def __init__(self, title, author, available_status):
        self.title = title
        self.author = author
        self.available_status = available_status


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book_object):
        return self.collection.append(book_object)
    
    def view_all_books(self):   
        for book in self.collection:
            print(f"Title: '{book.title}', Author: '{book.author}', Status: '{book.available_status}'")