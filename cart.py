class Cart():
    def __init__(self):
        self.items = {}
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items[device.name] = amount
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            print(f"Not enough {device.name} available")

    def remove_device(self, device, amount):
        if device.name in self.items:
            if self.items[device.name] >= amount:
                self.items[device.name] -= amount
                self.total_price -= device.price * amount
                device.stock += amount
            else:
                print(f"Not enough {device.name} in the cart")
        else:
            print(f"{device.name} is not in the cart")

    def get_total_price(self):
        return self.total_price
    
    def print_items(self):
        if self.items:
            for name, amount in self.items.items():
                print(f"{name}: {amount}")
        else:
            print("Your cart is empty")

    def checkout(self):
        if self.items:
            for name, amount in self.items.items():
                print(f"{name}\n")
        else: 
            print("Your cart is empty")
