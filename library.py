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
    def borrow_book(self,title):
        this_book=self.searche(title)
        
        if this_book is None:
            print("Book not found")
        elif this_book.is_borrowed:
            print("Already borrowed")
           
        else:
            this_book.is_borrowed = True
            print("borrowed successfully-")
    def return_book(self,title):
        this_book = self.searche(title)
        if this_book is None:
            print("not found")
        elif not this_book.is_borrowed:
            print("This book not borrowed")
        else:
            this_book.is_borrowed=False
            print("book was returned")
            
from models import Book
lib = Library()
lib.add_book(Book("Harry potter","J.K.Roeling",2007))
lib.add_book(Book("Spider man","Stanli",2004))
lib.return_book("Spider man")
lib.borrow_book("Spider man")
lib.borrow_book("Harry potter")
lib.return_book("Spider man")
lib.return_book("Spider man")
lib.return_book('abs')
lib.show_books()