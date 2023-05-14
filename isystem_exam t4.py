# TASK 4
# Library project

class Book():
    def __init__(self, author, name):
        self.author = author
        self.name = name

    def get_author_name(self):
        return f"author: {self.name}"

    def get_book_name(self):
        return f"author: {self.name}"

    def toString(self):
        return f"{self.author}, {self.name}"

class Library():
    def __init__(self, code):
        self.code = code
        self.books = []
        self.floor = []
        self.closet = []
        self.shelf = []

    # Add book to exact position:
    def add(self):
        self.books.append(input('Book author and book name: '))
        self.floor.append(input('Position Floor: '))
        self.closet.append(input('Position Closet: '))
        self.shelf.append(input('Position Shelf: '))


    # does the book exist inputted position:
    def contains(self, position) -> list:
        if position[0] in self.floor and position[1] in self.closet and position[2] in self.shelf:
            return True
        else:
            return False


    # GET - Floor, Closet, Shelf:
    def getFloor(self, name):
        return f"{self.floor.index(name)}"

    def getCloset(self, name):
        return f"{self.closet.index(name)}"

    def getShelf(self, name):
        return f"{self.shelf.index(name)}"

    # Returns all book names with author names togrther after their shelf names: e.g.: shelf1, shelf2, ...
    def getBooks(self):
        for i in range(len(self.shelf)):
            print(self.shelf[i])
            for j in range(len(self.books)):
                print(self.books[j])
        
    # Find a book:
    def find(self, author, name, books):
        return f"{author} {name}" if f"{author} {name}" in books else "Not found"


# Additional note: getBooks() woud be nested dict, what that dict contains the list of f"{Book.author} {Book.name}"s:
# e.g.:
# 
# library = {"floor1":{shelf1:["author1, name1", "author2, name2", "author3, name3", ...], 
#                      shelf1a:["author1a, name1a", "author2a, name2a", "author3a, name3a", ...],
#                      shelf1b:["author1b, name1b", "author2b, name2b", "author3b, name3b", ...]},
#                      ....
#            "floor2":{shelf2:["author4, name4", "author5, name5", "author6, name6", ...],
#                      shelf2a:[...],
#                      shelf2a:[...]},
#            "floor3":{shelf3:["author7, name7", "author8, name8", "author9, name9", ...],
#                       .... }
#   } 

# But I didn't know how to realize it like above.
