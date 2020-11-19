# Write my Book class
# Inherits from Book
# string title
# string author
# int price

# Book class abstract display() method so it prints 
# Title: $title
# Author: $author
# Price: $price

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book): # inherits from Book- class (see above)
    price = 0
    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print('Title: ' + title)
        print('Author: ' + author)
        print('Price: ' + str(price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()