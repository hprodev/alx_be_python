# library_management.py


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self._is_checked_out = False  # single _ signifies private

#     def check_out(self):
#         self._is_checked_out = True

#     def return_book(self):
#         self._is_checked_out = False

#     def is_available(self):
#         return not self._is_checked_out


class Bird:
    def fly(self):
        print("Bird is flying")


class Mammal:
    def run(self):
        print("Mammal is running")


class Bat(Bird, Mammal):
    def fly(self):
        print("Bat is flying")

    def run(self):
        print("Bat is running")


b = Bat()
b.fly()
b.run()


# class Library:
#     def __init__(self):
#         self._books = []

#     def add_book(self, book):
#         self._books.append(book)

#     def check_out_book(self, title):
#         for book in self._books:
#             if book.title == title and book.is_available():
#                 book.check_out()
#                 return
#         print(f"'{title}' is not available for checkout.")

#     def return_book(self, title):
#         for book in self._books:
#             if book.title == title and not book.is_available():
#                 book.return_book()
#                 return
#         print(f"'{title}' was not checked out or not found.")

#     def list_available_books(self):
#         available_books = [book for book in self._books if book.is_available()]
#         if not available_books:
#             print("No books available.")
#         else:
#             for book in available_books:
#                 print(f"{book.title} by {book.author}")
