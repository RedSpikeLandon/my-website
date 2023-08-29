class Book:

    def _init_(self, title, author, year, publisher, word_count):
        self.title = title
        self.author = author
        self.word_count = word_count
        self.publisher = publisher
        self.year = year

harry_potter = Book("Harry Potter", "J.K Rowling", "1998", "Bloomsburg", "1,000,000")
print(harry_potter.year)