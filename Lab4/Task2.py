from datetime import datetime


class OrderManager:
    def __init__(self, orders):
        self.__orders = orders

    def addOrder(self, other):
        self.__orders.append(other)

    # 6) Get all orders having products with a given category
    def getOrdersByCategory(self, categoryName):
        return [order for order in self.__orders
                for item in order.getItems() if item.getP().checkSameCategory(categoryName)]

    # 7) Get all products ordered by a customer with a tier of 2 from 01/2/2024 to 01/04/2024
    def getProductWithTier(self, tier, startDate, endDate):
        startDate = datetime.strptime(startDate, "%Y-%m-%d")
        endDate = datetime.strptime(endDate, "%Y-%m-%d")
        return [product.getP() for order in self.__orders
                if order.getCustomer().checkSameTier(tier) and startDate <= datetime.strptime(order.getOrderDate(),
                                                                                              "%Y-%m-%d") <= endDate
                for product in order.getItems()]

    # 8) Get 3 recent orders
    def get3ProductRecent(self):
        sortedOrder = sorted(self.__orders, key=lambda order: datetime.strptime(order.getOrderDate(), "%Y-%m-%d"),
                             reverse=True)
        return sortedOrder[:3]

    # 9) Get all orders ordered on 15/03/2024
    def getOrderByDate(self, date):
        dateRequest = datetime.strptime(date, "%d/%m/%Y")  # Parse the input date
        return [order for order in self.__orders if datetime.strptime(order.getOrderDate(), "%Y-%m-%d") == dateRequest]

    # 10) Cost of all orders in 2/2024
    def totalCostInDate(self, month, year):
        return sum(order.getTotalCostOrder() for order in self.__orders
                   if datetime.strptime(order.getOrderDate(), "%Y-%m-%d").month == month and
                   datetime.strptime(order.getOrderDate(), "%Y-%m-%d").year == year)

    # 11)Average cost of all orders bought on 15/03/2024
    def averageCostByDate(self, date):
        orders_on_date = self.getOrderByDate(date)
        return sum(order.getTotalCostOrder() for order in orders_on_date) / len(orders_on_date) if orders_on_date else 0

    # 12)Get statistics for each order and the number of products (key: oid, value: the
    # number of products in the corresponding order)
    def get_order_statistics(self):
        return {order.__oid: len(order.getItems()) for order in self.__orders}

    # 13)Get statistics of orders by customer (key: cid, value: list of orders bought by
    # the corresponding customer)
    def getStatisticsByCustomer(self):
        listCid = set(order.getCustomer().getCid() for order in self.__orders)
        return {cid: list(order for order in self.__orders if order.getCustomer().checkSameCid(cid))
                for cid in listCid}

    def getOrderCosts(self):
        return {order.getOid(): order.getTotalCostOrder() for order in self.__orders}


class Order:
    def __init__(self, oid, status, orderDate, deliveryDate, customer, items):
        self.__oid = oid
        self.__status = status
        self.__orderDate = orderDate
        self.__deliveryDate = deliveryDate
        self.__customer = customer
        self.__items = items

    def __repr__(self):
        return f"Order(oid={self.__oid}, customer={self.__customer.getCid()}, items={[(item.getQuantity(), item.getP()) for item in self.__items]})"
    def getOid(self):
        return self.__oid

    def getItems(self):
        return self.__items

    def getCustomer(self):
        return self.__customer

    def getOrderDate(self):
        return self.__orderDate

    def getTotalCostOrder(self):
        return sum(item.getP().getPrice() * item.getQuantity() for item in self.__items)

    # 1) Get all products belonging to a given category and their price values are higher than a given threshold
    def getProductByCategoryAndPrice(self, categoryName, price):
        return [item.getP() for item in self.__items
                if item.getP().getPrice() > price and item.getP().checkSameCategory(categoryName)]

    # 2) Get all products based on a given category and decrease their price to 10%
    def discountProductByCategory(self, categoryName):
        return [item.getP().setPrice(item.getP().getPrice() * 0.9)
                for item in self.__items if item.getP().checkSameCategory(categoryName)]

    # 3) Get the cheapest product in a given category
    def getProductCheapestByCategory(self, categoryName):
        products = [item.getP() for item in self.__items if item.getP().checkSameCategory(categoryName)]
        return min(products, key=lambda p: p.getPrice())

    # 4) Get statistics of products by category (key = category, value = products)
    def getStatistics(self):
        listCategory = set(item.getP().getCategory() for item in self.__items)
        return {k: list(item.getP() for item in self.__items if item.getP().checkSameCategory(k))
                for k in listCategory}

    # 5) Get the most expensive products by category (key = category, value = most expensive product)
    def getMostExpensiveProductByCategory(self):
        categories = {item.getP().getCategory() for item in self.__items}
        return {
            category: max(
                (item.getP() for item in self.__items if item.getP().checkSameCategory(category)),
                key=lambda p: p.getPrice(),
            )
            for category in categories
        }


class OrderItem:
    def __init__(self, quantity, p):
        self.__quantity = quantity
        self.__p = p

    def getP(self):
        return self.__p

    def getQuantity(self):
        return self.__quantity


class Product:
    def __init__(self, pid, name, category, price):
        self.__pid = pid
        self.__name = name
        self.__category = category
        self.__price = price

    def checkSameCategory(self, categoryName):
        return self.__category == categoryName

    def getPrice(self):
        return self.__price

    def getCategory(self):
        return self.__category

    def setPrice(self, newPrice):
        self.__price = newPrice

    def __repr__(self):
        return f"{self.__pid}, {self.__name}', {self.__category}', {self.__price}"


class Customer:
    def __init__(self, cid, name, tier):
        self.__cid = cid
        self.__name = name
        self.__tier = tier

    def getTier(self):
        return self.__tier

    def checkSameCid(self, cidOther):
        return self.__cid == cidOther

    def checkSameTier(self, otherTier):
        return self.__tier == otherTier

    def getCid(self):
        return self.__cid


# Example usage
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

om = OrderManager([order1])
# Add a new order
product4 = Product(4, "Tablet", "Electronics", 500)
order_item4 = OrderItem(1, product4)  # 1 Tablet
order2 = Order(2, "Pending", "2024-03-01", "2023-11-05", customer1, [order_item4])
om.addOrder(order2)

print(om.getOrdersByCategory("Electronics"))
print(om.get3ProductRecent())
print(om.getProductWithTier(2, "2024-02-01", "2024-04-01"))
print(om.getOrderByDate("15/03/2024"))
print(om.totalCostInDate(2, 2024))
print(om.getStatisticsByCustomer())
print(om.getOrderCosts())
