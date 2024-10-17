from Lab3.Task3.Publication import Publication


class Magazine(Publication):
    def __init__(self, title, numberOfPage, yearOfPublication, author, price, name):
        super().__init__(title, numberOfPage, yearOfPublication, author, price)
        self.name = name

    def __str__(self):
        return f"Magazine: {self.title}, {self.numberOfPage}, {self.yearOfPublication}, {self.author}, {self.price}, {self.name}"

    def typeOfPublication(self):
        return "Magazine"
