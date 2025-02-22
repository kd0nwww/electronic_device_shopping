class Device():
    def __init__(self, name, price, stock, warranty_period):

        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def __str__(self):
        return f"Device: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty Period: {self.warranty_period}"
    
    def display_info(self):
        print(f"Device: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}")

    def apply_discount(self, discount_percentage):
        discount = self.price * discount_percentage / 100
        self.price -= discount

    def is_available(self, amount):

        if self.stock >= amount:
            return True
        else:
            return False
        
    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
        else:
            print("Not enough stock available")
    
device = Device("Laptop", 1000, 10, 2)
device.apply_discount(23)
print(device.price)

print(device.reduce_stock(7))