from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return super().__str__() + f", Screen Size: {self.screen_size}, Battery Life: {self.battery_life}"
    
    def make_call(self):
        print(f"Smartphone {self.name} is making a call")

    def install_app(self):
        print(f"App is being installed on {self.name}")

    def display_info(self):
        print(f"Device: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}\nScreen Size: {self.screen_size}\nBattery Life: {self.battery_life}")