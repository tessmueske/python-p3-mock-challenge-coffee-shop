class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string")
        if not 3 <= len(value):
            raise ValueError("Coffee name must be greater than 3 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Coffee name cannot be changed")
        self._name = value
        
    def orders(self):
        coffee_list = []
        for order in Order.all:
            if order.coffee == self:
                coffee_list.append(order)
        return coffee_list

    def customers(self):
        customer_list = []
        for order in Order.all:
            if order.coffee == self and order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        price_list = []
        for order in Order.all:
            if order.coffee == self:
                price_list.append(order.price)
        # Returns the average price for a coffee based on its orders
        # Returns 0 if the coffee has never been ordered
        # Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
        average = sum(price_list) / len(price_list)
        return average

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be of type string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Customer name must be between 1-15 characters")
        self._name = value
        
    def orders(self):
        all_orders = []
        for order in Order.all:
            if order.customer == self:
                all_orders.append(order)
        return all_orders
    
    def coffees(self):
        unique_coffees = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in unique_coffees:
                    unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        Order.all.append(new_order)
        return new_order
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Coffee price cannot be changed")
        self._price = value