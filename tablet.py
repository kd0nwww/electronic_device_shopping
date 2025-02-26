from device import Device

class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return super().__str__() + f", Screen Resolution: {self.screen_resolution}, Weight: {self.weight}"
    
    def browse_internet(self):
        print(f"Internet is being browsed on {self.name}")

    def use_touch_screen(self):
        print(f"Touch screen is being used on {self.name}")
              
    def display_info(self):
        print(f"Device: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}\nScreen Resolution: {self.screen_resolution}\nWeight: {self.weight}")