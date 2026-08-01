"""
Magic methods = Dunder methods (double underscore) __init__ , __str__ , __eq__ , __add__ , __len__ , __getitem__ , __setitem__ ,
                                                        __delitem__ , __iter__ , __next__ , __call__ , __enter__ , __exit__, etc.

They are automatically called by many of Python's built-in operations.
They allow developers to define or customize the behavior of objects for built-in operations, such as addition, subtraction, string representation, and more.

"""

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages


    def __str__(self):
        return f"{self.title} by {self.author}, {self.num_pages} pages"

    def __len__(self):
        return self.num_pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.num_pages < other.num_pages
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Book):
            return self.num_pages > other.num_pages
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", f"{self.author} & {other.author}", self.num_pages + other.num_pages)
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.title or item in self.author
        return False

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien" , 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172) 

print(book1)  # Output: The Hobbit by J.R.R. Tolkien, 310 pages
print (book1 == book2)  # Output: False
print(book1  < book2)  # Output: False
print(book1  > book2)  # Output: True   
print(book1 + book2)  # Output: The Hobbit & Harry Potter and The Philosopher's Stone by J.R.R. Tolkien & J.K. Rowling, 533 pages
print("The Hobbit" in book1 )  # Output: True
print(book1["title"])  # Output: The Hobbit
print(book1["author"])  # Output: J.R.R. Tolkien
print(book1["num_pages"])  # Output: 310
print(book1["audio"])  # Output: Key audio was not found    