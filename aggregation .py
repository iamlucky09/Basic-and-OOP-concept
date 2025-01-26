# the concept of aggregation in python
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    # and this is for printing or displaying all the books at once uing loop
    def display_books(self):
        for boo in self.books:
            print(f"title:{boo.title}, aurthor:{boo.author}")



book1 = book("Rich Dad Poor Dad", "Robert Toru Kiyosaki")
book2 = book("The Intelligent Investor", "Benjamin Graham")

libra = library("pen")
libra.add_books(book1)
libra.add_books(book2)
libra.display_books() #yo chai loop layera sabai print garya ho

# euta matra book ko details print garna ko lagi chai ,we can do following 
print(f'Title: {book1.title}, Author: {book1.author}')

# and for the arko book lai print garna paryema 
print(f'Title: {book2.title}, Author: {book2.author}')
# yeso gareni huncha