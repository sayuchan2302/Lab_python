from Lab3.Task3.Publication import Publication


class Reference(Publication):
    def __init__(self, title, numberOfPage, yearOfPublication, author, price, field, chapters):
        super().__init__(title, numberOfPage, yearOfPublication, author, price)
        self.field = field
        self.chapters = chapters

    def __str__(self):
        return f"Reference: {self.title}, {self.numberOfPage}, {self.yearOfPublication}, {self.author}, {self.price}, {self.field}"

    def typeOfPublication(self):
        return "Reference"