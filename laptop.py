from device import Device

class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, proccessor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.proccessor_speed = proccessor_speed

    def __str__(self):
        return super().__str__() + f", RAM Size: {self.ram_size} GB, Proccessor Speed: {self.proccessor_speed} GHz"
    
    def run_program(self):
        print(f"Program is running on {self.name}")

    def use_keyboard(self):
        print(f"Keyboard is being used on {self.name}")

    def display_info(self):
        print(f"Device: {self.name}\nPrice: {self.price} USD\nStock: {self.stock}\nWarranty Period: {self.warranty_period} months\nRAM Size: {self.ram_size} GB\nProccessor Speed: {self.proccessor_speed} GHz")