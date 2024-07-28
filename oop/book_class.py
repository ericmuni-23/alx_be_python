#!/usr/bin/env python3
class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to print a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        
        Returns:
        str: A string in the format "(title) by (author), published in (year)".
        """
        return f"({self.title}) by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        
        Returns:
        str: A string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage:
book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book)  # Output: (To Kill a Mockingbird) by Harper Lee, published in 1960
print(repr(book))  # Output: Book('To Kill a Mockingbird', 'Harper Lee', 1960)
del book  # Output: Deleting To Kill a Mockingbird

class Book:
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints "Deleting (title of the book)" upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a string in the format "(title) by (author), published in (year)".
        """
        return f"({self.title}) by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage:
book1 = Book("Python Crash Course", "James Harden", 2019)
print(book1)  # Output: (Python Crash Course) by James Harden, published in 2019
print(repr(book1))  # Output: Book('Python Crash Course', 'James Harden', 2019)

del book1  # Output: Deleting Python Crash Course
