class Library:
    def __init__(self):
        books =[]
        self.books = books
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book)
    def searche(self, title):
        for book in self.books:
            if book.title == title:
                return book
            
        return None
from models import Book
lib = Library()
lib.add_book(Book("Harry potter","J.K.Roeling",2007))
lib.add_book(Book("Spider man","Stanli",2004))
result = lib.searche("Spider man")
print(result)