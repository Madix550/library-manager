class Library:
    def __init__(self):
        books =[]
        self.books = books
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book)
from models import Book
lib = Library()
lib.add_book(Book("Harry Poter", "J.K.Rowling", 2007))
lib.add_book(Book("Spider man","Stanli",2004))
lib.show_books()