from dataclasses import dataclass, field
from datetime import date

# class Book():
#     total_books = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#
#     def get_info(self):
#         print(f"Book: {self.title}, Author: {self.author}")
#
#     @classmethod
#     def get_total_books(cls):
#         print(f"Total books: {cls.total_books}")
#
#     @staticmethod
#     def is_valid_title(title):
#         return len(title) != 0

@dataclass
class Book:
    title: str
    year: int
    def __post_init__(self):
        if (self.year > date.today().year):
            raise ValueError("")

@dataclass
class Library:
    books: list[Book] = field(default_factory=list)
    def add_book(self, book: Book):
        self.books.append(book)

book1 = Book("", 1999)
book2 = Book("", 2000)
library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
print(len(library1.books), library1.books)
