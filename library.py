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
            print("borrowed successfully")

from models import Book
lib = Library()
lib.add_book(Book("Harry potter","J.K.Roeling",2007))
lib.add_book(Book("Spider man","Stanli",2004))
lib.borrow_book("Spider man")
lib.borrow_book("Harry potter")
lib.borrow_book("Spider man")
lib.borrow_book("Spider man")
lib.borrow_book('ll')
lib.show_books()