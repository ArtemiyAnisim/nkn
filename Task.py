class Book:
    def __init__(self, name, author, isbn):
        self.__name = name
        self.__author = author
        self.__isbn = isbn

        def get_author(self):
            return self.__author

        def set_author(self, author):
            self.__author = author

b = Book('name', 'author1', 12545588515155)
print(b.get_author())
b.set_author('jijfijf')
print(b.get_author())
