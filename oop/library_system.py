#!/usr/bin/env python3
class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
        title (str):  Title of the book.
        author (str): Author of the book.
        year (int): Publication year of the book.
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
book = Book("Think big", "Ben Carson", 1994)
print(book)  # Output: (To Kill a Mockingbird) by Ben Carson, published in 1994
print(repr(book))  # Output: Book('Think big', 'Ben Carson', 1994)
del book  # Output: Deleting Think big
