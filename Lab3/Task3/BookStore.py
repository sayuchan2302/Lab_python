class BookStore:
    def __init__(self, publications):
        self.publications = publications
    def sumCost(self):
        sum = 0
        for publication in self.publications:
            sum += publication.price
        return sum
    def isMagazineInStore(self, name):
        for publication in self.publications:
            if publication.typeOfPublication() == "Magazine" and publication.name == name:
                return True
        return False
    def findReferenceWithMostPagesChapter (self) :
        maxPages = 0
        maxReference = None
        for publication in self.publications:
            if publication.typeOfPublication() == "Reference":
                reference = publication
                for chapter in reference.chapters:
                    if chapter.numberOfPages > maxPages:
                        maxPages = chapter.numberOfPages
                        maxReference = reference
        return maxReference