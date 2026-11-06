class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"
        return f"{self.title} - {self.author} - ({self.year}) - [{status}]"