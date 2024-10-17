class OrderManager :
    def __init__(self , orders):
        self.__orders = orders
class Order :
    def __init__(self , oid , status , orderDate , deliveryDate , customer , items):
        self.__oid = oid
        self.__status = status
        self.__orderDate = orderDate
        self.__deliveryDate = deliveryDate
        self.__customer = customer
        self.__items = items
    #1) Get all products belonging to a given category and their price values are higher than a given threshold
    def getProductByCategoryAndPrice (self , categoryName , price) :
        return [item.getP() for item in self.__items
                if item.getP().getPrice() > price and item.getP().getCategory() == categoryName]
    #2) Get all products based on a given category and decrease their price to 10%
    def discountProductByCategory (self , categoryName) :
        return [item.getP().setPrice(item.getP().getPrice() * 0.9)
                for item in self.__items]
    #3) Get the cheapest product in a given category
    def getProductCheapestByCategory(self , categoryName):
        products = [item.getP() for item in self.__items if item.getP().getCategory() == categoryName]
        return min (products , key = lambda p : p.getPrice())
    #4) Get statistics of products by category (key = category, value = products)
    def getStatistics (self) :
        listCategory = set(item.getP().getCategory() for item in self.__items)
        # return {k : list (item.getP() for item in self.__items if item.getP().getCategory == k)
        #         for k in listCategory}
        return {k: list(item.getP() for item in self.__items if item.getP().getCategory() == k)
                for k in listCategory}
    #5) Get the most expensive products by category (key = category, value = most expensive product)
    def getMostExpensiveProductByCategory(self):
        categories = {item.getP().getCategory() for item in self.__items}
        return {
            category: max(
                (item.getP() for item in self.__items if item.getP().getCategory() == category),
                key=lambda p: p.getPrice(),
            )
            for category in categories
        }

class OrderItem :
    def __init__(self , quantity , p):
        self.__quantity = quantity
        self.__p = p
    def getP(self):
        return self.__p
class Product :
    def __init__(self , pid , name , category , price ) :
        self.__pid = pid
        self.__name = name
        self._category = category
        self._price = price
    def getPrice (self) :
        return self._price
    def getCategory (self) :
        return self._category
    def setPrice (self , newPrice) :
        self._price = newPrice
    def __repr__(self):  # Add __repr__ method to Product
        return f"{self.__pid}, {self.__name}', {self._category}', {self._price}"
class Customer :
    def __init__(self , cid , name , tier):
        self.__cid = cid
        self.__name = name
        self.__tier = tier

product1 = Product(1, "Laptop", "Electronics", 1200)
product2 = Product(2, "Phone", "Electronics", 800)
product3 = Product(3, "Book", "Books", 30)
order_item1 = OrderItem(1, product1)  # 1 Laptop
order_item2 = OrderItem(2, product2)  # 2 Phones
order_item3 = OrderItem(1, product3)  # 1 Book

customer1 = Customer(1, "Alice", 2)

order1 = Order(1, "Completed", "2023-10-17", "2023-10-20", customer1, [order_item1, order_item2, order_item3])
# Test getProductByCategoryAndPrice (Electronics category with price > 900)
result = order1.getProductByCategoryAndPrice("Electronics", 900)
print(result)
order1.discountProductByCategory("Electronics")
print("\ndiscount 10%")
result1 = order1.getProductByCategoryAndPrice("Electronics", 0)  # Now, just to see all Electronics products
print(result1)

print("Cheapest: " + str(order1.getProductCheapestByCategory("Electronics")))
print(order1.getStatistics())
print(order1.getMostExpensiveProductByCategory())