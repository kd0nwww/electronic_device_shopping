from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, proccessor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.proccessor_speed = proccessor_speed

    def __str__(self):
        return super().__str__() + f", RAM Size: {self.ram_size}, Proccessor Speed: {self.proccessor_speed}"
    
    def run_program(self):
        print(f"Program is running on {self.name}")

    def use_keyboard(self):
        print(f"Keyboard is being used on {self.name}")

    def display_info(self):
        print(f"Device: {self.name}\nPrice: {self.price}\nStock: {self.stock}\nWarranty Period: {self.warranty_period}\nRAM Size: {self.ram_size}\nProccessor Speed: {self.proccessor_speed}")

    
laptop = Laptop("Dell XPS 13", 1299.99, 50, 12, "16GB", "2.8GHz")
laptop.display_info()