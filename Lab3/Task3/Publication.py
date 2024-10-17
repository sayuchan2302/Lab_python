from abc import ABC, abstractmethod

class Publication(ABC):
    def __init__(self, title, numberOfPage, yearOfPublication, author, price):
        self.title = title
        self.numberOfPage = numberOfPage
        self.yearOfPublication = yearOfPublication
        self.author = author
        self.price = price

    @abstractmethod
    def typeOfPublication(self):
        pass

    def isMagazine10YearOld(self):
        if self.typeOfPublication() == "Reference":
            return False  # References are not magazines
        else:
            return 2024 - self.yearOfPublication >= 10

    def checkSameAuthor(self, other):
        return self.author == other.author