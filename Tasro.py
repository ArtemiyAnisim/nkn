class Publication:
    def __init__(self, title, author, year ):
        self.title = title
        self.author = author
        self.year = year


    def display(self):
        print('Название:', self.title)
        print(f'Автор: {self.author}')
        print(f'Год издания {self.year}')


class Book(Publication):
    def __init__(self, title, author, year, issue_number):
        super(Book, self).__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
       super(Book, self).display()
       print(f'Номер журнала: {self.issue_number}')



p = Publication('Название1', "Автор1", 2015)
p.display()
print()
b = Book("Название2", "Автор2", 2021, 46576454538764)
b.display()
print()


