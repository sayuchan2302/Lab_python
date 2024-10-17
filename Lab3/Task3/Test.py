from Lab3.Task3.BookStore import BookStore
from Lab3.Task3.Chapter import Chapter
from Lab3.Task3.Magazine import Magazine
from Lab3.Task3.Reference import Reference

chapter1 = Chapter("Introduction to Programming", 20)
chapter2 = Chapter("Advanced Topics in Programming", 35)
chapter3 = Chapter("Data Structures", 40)
chapter4 = Chapter("Operating Systems", 45)
chapter5 = Chapter("Networking Fundamentals", 30)
chapter6 = Chapter("Database Management", 50)
chapter7 = Chapter("Introduction to AI", 25)
chapter8 = Chapter("Machine Learning", 40)
chapter9 = Chapter("Deep Learning", 35)

magazine1 = Magazine("Tech Innovators", 80, 2003, "John Doe", 15.99, "Tech Monthly")
magazine2 = Magazine("Science Digest", 90, 2020, "Alice Johnson", 12.99, "Science Monthly")
reference1 = Reference("Programming Handbook", 250, 2022, "John Doe", 45.00, "Computer Science", [chapter1, chapter2, chapter3])
reference2 = Reference("Computer Science Basics", 300, 2020, "Alan Turing", 55.00, "Computer Science", [chapter4, chapter5, chapter6])
reference3 = Reference("AI Guide", 320, 2021, "Andrew Ng", 60.00, "Artificial Intelligence", [chapter7, chapter8, chapter9])
bookstore = BookStore([magazine1,magazine2, reference1, reference2 , reference3])

print(bookstore.publications[0].typeOfPublication())
print(bookstore.publications[3].typeOfPublication())

print(bookstore.publications[0].isMagazine10YearOld())
print(bookstore.publications[2].isMagazine10YearOld())

print(bookstore.publications[0].checkSameAuthor(bookstore.publications[2]))
print(bookstore.publications[0].checkSameAuthor(bookstore.publications[2]))

print(bookstore.findReferenceWithMostPagesChapter())
print(bookstore.isMagazineInStore("Tech Monthly"))
print(bookstore.isMagazineInStore("Unknown Monthly"))
print ("Sum cost:" ,bookstore.sumCost())