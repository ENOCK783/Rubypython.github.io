#parent class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        return f"The title {self.title} {self.author} {self.year}"

#child class/derived class

class libraryBook(Book):
    def __init__(self, title, author, year, isbn,copies_available):
        super().__init__(title, author, year)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f" {self.title} borrowed. copies left: {self.copies_available}"
        else:
            return f"no of copies {self.title} unavailable"
    def return_book(self):
        self.copies_available += 1
        return f" {self.title} returned. copies left: {self.copies_available}"

    #usage example
book1 = libraryBook("inheritance", "adrian", 1999, 1999, True)
print(book1.display_info())
book1.borrow_book()
print(book1.return_book())