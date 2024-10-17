class Chapter:
    def __init__(self, title, numberOfPages):
        self.title = title
        self.numberOfPages = numberOfPages

    def __str__(self):
        return f"Chapter: {self.title}, {self.numberOfPages}"